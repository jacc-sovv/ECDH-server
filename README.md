To run on the CSU machines, there's a few things you need to do.  
1) We'll have to use the right version of python. To do this, type module load python/bundle-3.9.  
  a) If this doesn't work, that means you have another module of python loaded. Keep track of which module you have (the command which python should help) in case you want to re-load it once we're done with this project. If you do have another python loaded, you will have to do 'module unload python' first, then module load python/bundle-3.9
2) Install the cryptography library by:
```bash
pip3 install cryptography --user
export PATH="~/.local/bin:$PATH"
export PYTHONPATH="~/.local/lib/python3.x/site-packages/:$PYTHONPATH"
```
3) Run the server! After the server is running, then you can run cerberus.
