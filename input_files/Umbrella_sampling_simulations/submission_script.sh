
#------------------CP2K variables------------------------------------
cp2k_input=run_nvt.inp
cp2k_input_aux=cp2k.aux
cp2k_output=cp2k.out
cp2k_error=cp2k.err
options="-i ${cp2k_input_aux} > ${cp2k_output} 2> ${cp2k_error}  "
CMD_CP2K="mpirun -ppn $mpi_tasks_per_node -np $np cp2k.popt $options"


#------------------i-PI variables------------------------------------
IPI_EXE=/home/yl899/codes/i-pi/bin/i-pi
HOST=$(hostname)
NTIME=43200 # 12 hs

#-----------------------------------------
echo  {"init",$( date -u)} >>LIST
grep '<step>'  RESTART >> LIST

######### CHECK RESTART FILE ###############
if [ ! -f "RESTART"   ]
 then
  cp input.xml RESTART
fi
grep 'plumed_extras' RESTART -v >o
mv o RESTART
######### CHECK RESTART FILE ###############

rm -f /tmp/ipi_${HOST}

# Prepare stuff i-pi
 sed -e "s:<address>.*:<address>$HOST</address>:" RESTART > RESTART.tmp1
 sed -e "s:<total_time>.*:<total_time>$NTIME</total_time>:" RESTART.tmp1 > INITIAL.xml

# Prepare stuff cp2k
 sed -e "s/ipihost/$HOST/g" ${cp2k_input} > ${cp2k_input_aux}


# Run the program:

rm -f EXIT

echo 'launch i-pi'
   python3 -u ${IPI_EXE} INITIAL.xml &> ipi.out &
   sleep 20
echo 'launch cp2k'
    eval ${CMD_CP2K}
sleep 15
touch EXIT
sleep 15

###############  After run checks ######################################################

 # save data
 echo '1' >>count
 l=`cat count|wc -l`
 mkdir -p OUTPUT
 cp cp2k.out OUTPUT/cp2k_${l}.out
 cp cp2k.err OUTPUT/cp2k_${l}.err
 grep 'STEP_START_VAL' ${restart_filename} >>LIST
 echo  {"Final and restart",$( date -u)} >>LIST

cp ipi.out log.ipi

var1=$( grep 'Simulation has already run for total_steps, will not even start' log.ipi  )
if [ ! -z "$var1" ]
   then
       echo 'finished' #>>LIST
       touch STOP
   else
       echo 'not finished' #>>LIST
fi

var1=$( grep 'INITIAL.xml:1:0: no element found' log.ipi  )
if [ ! -z "$var1" ]
   then
       echo 'PROBLEM REINIT' #>>LIST
       touch STOP
   else
       echo 'not finished' #>>LIST
fi

var1=$( grep 'IOError: [Errno 2] No such file or directory:' log.ipi  )
if [ ! -z "$var1" ]
   then
       echo 'PROBLEM ' #>>LIST
       touch STOP
   else
       echo 'not finished' #>>LIST
fi

 #################### Resubmit #################################3
 if [ ! -f "STOP"   ]
    then
        sbatch submission_script.sh 
    else
        echo "Stop file is found" >>LIST
 fi

