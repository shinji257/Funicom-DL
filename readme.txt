Funicom-DL
by Pikanet128

Instrutctions ~

0. Install python ver 2.7.x
1. Clear out the Funicom-DL.que if you want.
2. Add the -G and your choice of language and quality to the first line. example: -G -l e -q 480
-l e means English
-q 480 means the quality is 480p
-G means global - it also says im not a url don't dl me - but apply all cmds after me to everything until you see me again
3. Now all you have to do is post all the links to the episodes of the show you want.
4. Save
5. Run the Funicom-DL.bat and you're good to go


quefile example ~

-G -l e -q 480
URL of episode 1 here
URL of episode 2 here

And so on. You can change the 480 to 720 or 1080 if you want the high quality.


To note ~

You have to be connected to an american VPN (Or live there!) Hide.me is an example if it is not working for you. (MK edited)
can't help you on this as its not a problem for me


Full Command list ~

-G  = --global        = set global cmds  = {any other cmds}                      ## must be instead of url
-Q  = --quit          = quit the program = {}                                    ## must be instead of url
-l  =                 = language         = {e,eng,j,jpn,d,dub,s,sub}             ## still working on trailer and clip support
-q  =                 = quality          = {b,best,1080,1080p,720,720p,480,480p} ## if left out best is default
                                                                                 ## best could be 'be' or 'bes'
                                                                                 ##   same with 'en', 'jp', 'du' or 'su'
-fb =                 = fall back        = {} use with '-l e'                    ## falls back from eng to jpn if no eng
-io =                 = info only        = {}                                    ## only grab the info files
-fq =                 = force quality    = {}                                    ## force the quality
                                                                                 ## sometimes a vid is avalibale but
                                                                                 ##   funi did not add it to the html
                                                                                 ## don't use with 480p its useless
-fl =                 = force lang       = {} specify lang                       ## mostly for when dubs are just released and not
                                                                                 ##   added to the html
                                                                                 ##   does not work as much anymore
-b  =                 = pick bitrate     = {4000,3500,2500,2000,1500,1000,750}   ## this does not check if your resolution choice matches
                                                                                 ##   ex. if you put -q 1080p -b 2000K
                                                                                 ##   you will get 480p labled as 1080p
                                                                                 ## can also have a "K" at the end
                                                                                 ## ex. 2000K or 2000k

-------------------------------
ex.
-G -l e -fb
%url1%
%url2%
## all urls will try to dl dub if no dub then sub in the best quality (-q omitted = -q best)
-G -l e
%url1%
%url2%
-G -l j
%url3%
%url4%
## all urls will be in the best quality (-q omitted = -q best)## 1-2 will be dub## 3-4 will be sub
-G -l e -fb
%url1%
%url2%
%url3% -q 480p
## all urls will try to dl dub if no dub then sub in the best quality (-q omitted = -q best) execpt url3 will be 480p
-G -l e -fl -fq -q 1080p
%url1%
%url2%
## all urls will be forced to dub in 1080p if not then skipped


for ini instrutions see ini
for more que instrutions see que
