# Packet Analysis
Inspect the packets captured in this file and find the flag.

## Summary
+ **Author:** Jerald Yeo
+ **Discord Tag:** maximus#4723
+ **Category:** Forensics
+ **Difficulty:** Easy

## Solution
1. By following the TCP stream of any FTP packet, we can see that the user logs in and downloads 3 files: `one.png`, `two.png`, `three.png`.

    > RETR one.png  
      150 Opening BINARY mode data connection for one.png (137185 bytes).  
      226 Transfer complete.  
    > ...  
    > RETR two.png  
      150 Opening BINARY mode data connection for two.png (6639 bytes).  
      226 Transfer complete.  
    > ...  
    > RETR three.png  
      150 Opening BINARY mode data connection for three.png (5206 bytes).  
      226 Transfer complete.  

    The RETR command is issued when the client wants to download a copy of the file from the server.

2. To view the images that were downloaded by the client, right-click > Follow > TCP Stream on a FTP-DATA packet for a downloaded file (e.g `one.png`).
3. Change the `Show data as` option to `Raw` and save as a `.png` file.
4. Go through this process for the other 2 files. `two.png` and `three.png` show the flag when combined.

## Flag
```
YCEP2023{3XP0R71NG_F7P_F1L35_15_C00L}
```