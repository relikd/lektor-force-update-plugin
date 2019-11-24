# Force Update

Update resources regardless of changed state.
Usefull for, e.g., `.appcache` files.


## Configuration file

### `configs/force-update.ini`

    enabled = yes
	endswiths = .appcache, .webmanifest, ...

Where `endswiths` is a list of patterns (e.g., file extensions) of files that need a forced update.