# Time2
I made this link opener so I could buy Burning Man tickets in 2022. 

After missing the window to buy tickets to Burning Man by half a second and missing out, I realized I could use 
a cron job to schedule links to be opened ahead of time at exactly the date and time I wanted. I'm aware of the debate of the moral 
questionability surrounding ticket bots, so I didn't want to go the extra step and automate the payment, I just wanted something that would help
me react a bit faster.

This script takes in a link and a date and time and schedules an event that will open a browser window at the appointed time.
Since Cron jobs are generally intented to be repeated, I made it so the event will delete itself afterwards unless specificed.
That said, I could see the benefit of having certain links scheduled to open at certain regular times (e.g. expense report link at the end of every month)
