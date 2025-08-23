# rmpc

1. Find the user configuration directory. It can be at
    - $XDG_CONFIG_HOME/rmpc/
    - $HOME/.config/rmpc/
2. Create a directory called `themes` if it doesn't already exist
3. Put the `ashen.ron` file into this directory
4. Update `config.ron` to use ashen.

```ron
(
  ...
  theme: "ashen",
  ...
)
```
