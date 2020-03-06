# slurm-cat
Concatenate many SLURM files

See [RFC8416](https://tools.ietf.org/html/rfc8416) Simplified Local Internet Number Resource Management with the RPKI (SLURM)

# usage
Just like `cat` but for SLURM files.
```
$ ./slurm-cat.py slurm-1.json slurm-2.json slurm-3.json 
...
$
```

# Notes
As section [4.2](https://tools.ietf.org/html/rfc8416#section-4.2) of RFC8416 says:
```
4.2.  Multiple SLURM Files

   An implementation MAY support the concurrent use of multiple SLURM
   files. ...
```
This is simply a proof of concept code and can be used for RPKI systems where only one SLURM file is permitted (notice the **MAY** above).
