# Project 4:  Brevet time calculator w/ Ajax

## Nosetests
After executing the run.sh file, nosetests can be executed using the command 'docker exec -it $(docker ps --format '{{.Names}}') 'nosetests''

## Info

Implement the RUSA ACP controle time calculator with flask and ajax.

Credits: Micheal Young

Edited: Davis Bosworth

## ACP controle times

That's "controle" with an 'e', because it's French, although "control"
is also accepted.  Controls are points where   
a rider must obtain proof of passage, and control[e] times are the
minimum and maximum times by which the rider must  
arrive at the location.   

The algorithm for calculating controle times is described at
https://rusa.org/octime_alg.html 
More info here ~ https://rusa.org/pages/rulesForRiders. 

We are essentially replacing the calculator at
https://rusa.org/octime_acp.html 

This algorithm makes use of a table which contains minimum and maximum speeds for given control locations in km, including 200km, 400km, 600km, and 1000km. Open time calculation requires dividing the first 200km (or less if the control time is less than 200) by its maximum speed and so on until we reach the specified control time. Each speed segment is then added together to get the total time taken. This same algorithm is used for closing time calculations with the exception that we are now dividing by the minimum speed instead. After calculating both opening and closing times for a given brevet control distance, this value is then updated in the html table of distances and times. 

Warning: The calculator will allow routes not within the ACP rules. Check the ACP rules for further information on what does/doesn't make a route acceptable.
