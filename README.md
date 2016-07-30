# helpful_scripts

These are a small handful of scripts I've written over the past year or 2 that have helped with small tasks on my system. They're not complicated but each serves a specific purpose and reduces admin time considerably. 
Many of the scripts can be chained together to produce more useful work; an example of this would be "updateHashAndTree" which makes use of "tree", "getHash", and "updateTreeFile.py" to eliminate any manual work that needs to be done in hashing files and maintaining a file-tracking file.
Small modifications can be made to the scripts to make them more useful, e.g. "getHash" can be quickly modified to comapre old and new hash values to check for data integrity. 

The scripts should contain sufficient comments to understand what they are doing. Most have a header comment that talks about the purpose of the script. 

Some scripts are macOS specific, others will work just fine on other *nix. The macOS specific scripts are mostly in relation to handling disk image files with hdiutil.

The only word of caution I have is in regards to DMGmount - mountData chain. DMGmount takes a password and hands it off to a remote server over SSH, where mountData then decrypts a PW file. The PW file lives unencrypted on the remote system between hdiutil calls (very short). This is not a security risk for my needs but it's very easy to envision circumstances where this would be unacceptable security practice. 
