#!/bin/bash

#################################
    #COMMAND LINE ARGUMENTS#
#################################

#./termOPT.sh -a Algorithm -n listLength -e entropy -s seed(optional) -p precision(optional) -i iterations -x cut(optionnal)
#example :
#./termOPT.sh -a BubbleSort -n 10 -e 0.5 -s 123 -i 3

#the differents command line arguments and their conditions
while getopts ':a:n:e:s:p:i:x:' opt; do
    case "$opt" in

        a)  # Specify algorithm
            a=${OPTARG}    
            #check if the given algorithm is a string  
            if ! [[ "$a" =~ ^[a-zA-Z0-9]+$ ]]
                then
                    echo "error_ : [-a] takes a String for argument"
                    exit 0
            fi
        ;;

        n)  # Specify list length
            n=${OPTARG}
            #check is the length of the list is between 1 and 999 999
            if ! [[ "$n" =~ ^[^-0a-zA-Z+][0-9]{0,5}$ ]] 
                then
                    echo "error_ : [-n] takes an integer ( from 1 to 999 999 ) for argument"
                    exit 0
            fi            
        ;;

        e)  # Specify entropy
            e=${OPTARG}
            #check if the entropy is a float
            if ! [[ "$e" =~ ^[0-9]+"."[0-9]{1,8}$ ]]
                then
                    echo "error_ : [-e] takes a float ( with a maximum of 8 decimals ) for argument"
                    exit 0
            fi
        ;;    

        s)  # Specify seed ( optionnal )
            s=${OPTARG}  
            #check if the given seed is an interger or different than "" ( because it is optionnal )
            if ! [[ "$s" =~  ^[0-9]+$ ]] || [[ "$s" =~ ^.{0}$ ]] 
                then
                    echo "error_ : [-s] takes an integer for argument"
                    exit 0
            fi
        ;;  

        p) # Specify the precision applied to the entropy
            p=${OPTARG}
            #check if the precision seed is a float or different than "" ( because it is optionnal )
            if ! [[ "$p" =~ ^[0-9]+"."[0-9]{1,8}$ ]] || [[ "$p" =~ ^.{0}$ ]] 
                then 
                    echo "error_ : [-p] takes a float for argument. The default precision is 1.000"
                    exit 0     
            fi
        ;;

        i)  # Specify number of time you want the algorithm to be executed
            i=${OPTARG}
            #check if the number of iteration is an integer between 1 and 999 999
            if ! [[ "$i" =~ ^[^-0a-zA-Z+][0-9]{0,5}$ ]]      
                then
                    echo "error_ : [-i] takes an integer ( from 1 to 999 999 ) for argument"
                    exit 0
            fi
        ;; 

        x)
            x=${OPTARG}
            #check if the given x is "cut"
            if ! [[ "$x" =~ [cut] ]]
                then
                    echo "error_ : [-x] takes only "cut" for argument"
                    exit 0
            fi
        ;;

        ?)  #in case an unknown option is given
            echo "Usage : $(basename $0) [-a] [-n] [-e] [-s] [-p] [-i] [-x]"
            exit 1
        ;;
    esac
done       




argTermUseCut()
{
     
    ss_base=`expr $s / $i`      #ss_base is the seed divided by the number of iterations
                                #expr doesn't appreciate floating so ss_base is rounded down
                                    #so the results are not that precise
    ss_=$ss_base                #ss_ is the seed we will increase in the loop and use in the command 
    z=0
    if [[ $s == "" ]] && [[ $p == "" ]]
        then 
            while [[ $z -ne $i ]]
            do
                
                ((z=z+1))
                python3 TERM.py -a "$a" -n "$n" -e "$e"
                echo "__________________________________________________________"
            done
    fi

    
    if [[ $p == "" ]]
        then 
            while [[ $z -ne $i ]]
            do
                
                echo "Seed actuelle " $ss_
                ((z=z+1))
                python3 TERM.py -a "$a" -n "$n" -e "$e" -s "$ss_"
                ((ss_=ss_+ss_base))
                echo "__________________________________________________________"
            done
    fi

    if [[ $s == "" ]]   
        then 
            while [[ $z -ne $i ]]
            do
                
                ((z=z+1))
                python3 TERM.py -a "$a" -n "$n" -e "$e" -p "$p"
                echo "__________________________________________________________"
            done
    fi


    if [[ $p != "" ]] && [[ $s != "" ]]
        then
            while [[ $z -ne $i ]]
                do
                    
                    echo "Seed actuelle " $ss_
                    ((z=z+1))
                    python3 TERM.py -a "$a" -n "$n" -e "$e" -s "$ss_" -p "$p"
                    ((ss_=ss_+ss_base))
                    echo "__________________________________________________________"
                done
    fi
}

#according to the differents variables given, argTermUse perform the chosen algorithm -i times
argTermUse ()
{
    z=0
    if [[ $s == "" ]] && [[ $p == "" ]]
        then 
            while [[ $z -ne $i ]]
            do
                
                ((z=z+1))
                python3 TERM.py -a "$a" -n "$n" -e "$e"
                echo "__________________________________________________________"
            done
    fi

    
    if [[ $p == "" ]]
        then 
            while [[ $z -ne $i ]]
            do
                
                ((z=z+1))
                python3 TERM.py -a "$a" -n "$n" -e "$e" -s "$s"
                echo "__________________________________________________________"
            done
    fi

    if [[ $s == "" ]]   
        then 
            while [[ $z -ne $i ]]
            do

                
                ((z=z+1))
                python3 TERM.py -a "$a" -n "$n" -e "$e" -p "$p"
                echo "__________________________________________________________"
            done
    fi


    if [[ $p != "" ]] && [[ $s != "" ]]
        then
            while [[ $z -ne $i ]]
                do
                    
                    ((z=z+1))
                    python3 TERM.py -a "$a" -n "$n" -e "$e" -s "$s" -p "$p"
                    echo "__________________________________________________________" 
                done
    fi
}


if [[ $x == "cut" ]]
    then  
        if [[ $s != "" ]]           #a seed must be given
            then 
                argTermUseCut $a $n $e $s $p $i 
            else    
                echo "error_ : you forgot the seed"
                exit 0
        fi
    else
        argTermUse $a $n $e $s $p $i 
fi





