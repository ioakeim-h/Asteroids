A simple video game based on the classic [Asteroids](https://en.wikipedia.org/wiki/Asteroids_(video_game)).
You can take a look at this (slightly different from mine) [version of the game](https://www.echalk.co.uk/amusements/Games/asteroidsClassic/ateroids.html).

## Running in WSL

1. Add the XDG_RUNTIME_DIR environment variable for pygame:
```bash
export XDG_RUNTIME_DIR=/tmp/runtime-$USER
mkdir -p $XDG_RUNTIME_DIR
chmod 700 $XDG_RUNTIME_DIR
```

2. Install an X server on Windows (VcXsrv)
3. Start the X server on Windows before running your pygame app.
4. In your WSL terminal, set the display environment variable: `export DISPLAY=localhost:0`
5. Run your pygame script.