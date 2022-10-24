## maltrail-dups-cleaner

Auxiliary tool for trails deduplication. Can be useful for Maltrail's contributors to avoid adding trails (IP:port/domains/other type of trails), if they are already contained in static Maltrail bases.

## Common postulates

1) Basic scheme: contributor puts an input file, which contains list of trails. Maltrail-dups-cleaner checks this list for trails, that are already present in static Maltrail bases (```\maltrail-master\trails\``` folder) and returns the list with trails, that are guaranteedly absent in static bases. Optionally, but very desirably, Maltrail's whitelist can be connected as the filter.

![maltrail-dups-cleaner-scheme-800600](https://user-images.githubusercontent.com/7167300/196703734-b3193443-be36-4907-814e-76f3c7550be9.png)

2) Input file format: plain-text, new-line separated list of trails to filter with no junk symbols and\or spaces. For example:

![image](https://user-images.githubusercontent.com/7167300/196706232-3c41d1c3-b036-476f-9460-e6a0009477a1.png)

```maltrail-dups-cleaner``` proceeds search with strict compliance. For example: ```x.x.x.x:443``` and ```x.x.x.x:4431``` strings are given. If Maltrail bases contain ```x.x.x.x:4431``` trail, it would get filtered, but ```x.x.x.x:443``` would be counted as the candidate to get added.

## CLI management keys

![image](https://user-images.githubusercontent.com/7167300/196686259-9f994452-077e-42fd-917f-ea453016495c.png)


## Example of usage

Contributor has an input list, with trails he wants to add to Maltrail's static ```/cobaltstrike.txt``` base.

He runs in ```cmd``` or ```terminal```:

```duplicate_cleaner.py -i d:\cs4.txt -s c:\maltrail-master\maltrail-master\trails\static\ -w c:\maltrail-master\maltrail-master\misc\whitelist.txt -o d:\cs4_filtered.txt```



Here contributor gets ```d:\cs4_filtered.txt``` as the output file, filtered for duplications and whitelisted records, with trails ready to get added to target static Maltrail base (e.g.```/cobaltstrike.txt```).

## License

This software is provided under a MIT License as the original [Maltrail project](https://github.com/stamparm/maltrail/blob/master/README.md#license). See the accompanying [LICENSE](https://github.com/stamparm/maltrail/blob/master/LICENSE) file for more information.

## Links:

[Maltrail Project](https://github.com/stamparm/maltrail)

[Maltrail Wiki](https://github.com/stamparm/maltrail/wiki)
