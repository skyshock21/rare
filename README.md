# Output Character Count From File, Starting With Rarest Occurrences

The script rare.py allows you to input a text file, and it will output a count of each character's occurrence in the file beginning with those occurring the least amount of times.  This can be useed for instance to create a frequency distribution to aid in substitution cipher cryptanalysis.  It can serve as a library to be imported as well.  

## Run Application

In the directory where the script is stored run:

```
python rare.py SomeFile.txt
```

If running properly you should see a list of each character, along with the the count of how many times that character occurs in the file. The list will be ordered by least amount of occurrence first.
