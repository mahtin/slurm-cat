# slurm-cat
Concatenate many SLURM files

See [RFC8416](https://tools.ietf.org/html/rfc8416) Simplified Local Internet Number Resource Management with the RPKI (SLURM)

# Usage
Just like `cat` but for SLURM files.
```
$ ./slurm-cat.py slurm-1.json slurm-2.json slurm-3.json > slurm-total.json
$
```

# Sample files

For testing purposes; the following files are provided. The names are self-documenting.

* slurm-empty.json
* slurm-example.json
* slurm-prefixAssertions.json
* slurm-prefixFilters.json

The `slurm-empty.json` and `slurm-example.json` files come from RFC8416.

# Notes
As section [4.2](https://tools.ietf.org/html/rfc8416#section-4.2) of RFC8416 says:
```
4.2.  Multiple SLURM Files

   An implementation MAY support the concurrent use of multiple SLURM
   files. ...
```
This is simply a proof of concept code and can be used for RPKI systems where only one SLURM file is permitted (notice the **MAY** above).

# License

BSD License - see LICENSE.txt

