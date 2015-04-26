`ralph`
=======


```
                                       (\
                                        \\
                                         ))
                                        //
                                 .-.   //  .-.
                                /   \-((=-/   \    /~~~~~~~~~~~~~~~~~~~~~~~~~~~+
                                \      \\     /   / Hey there! I'm Ralph, your |
 $ ralph # Magic...              `( ____))_ )`   <  personal alias apprentice. |
                                 .-'   //  '-.    \ How can I serve you today? |
                                /     ((      \    \~~~~~~~~~~~~~~~~~~~~~~~~~~~+
                               |       !       |
                                \             /
                                 \   |___|   /
                                 _)  \   /  (_
                               (((---'   '---)))
```

### Create a *Blueprint*
![blueprint](https://cloud.githubusercontent.com/assets/1139621/7335747/8b64fe6a-eb98-11e4-818a-663748c3efdd.png)

### Ask Ralph to Work His *Magic*
![magic](https://cloud.githubusercontent.com/assets/1139621/7335748/8b71f5fc-eb98-11e4-97ca-34dbab476b68.png)

### Feel *Groovy* Using Your New Alias!
![alias](https://cloud.githubusercontent.com/assets/1139621/7335749/8b7329b8-eb98-11e4-8858-5d4ed0ab4fff.png)

## Designing a Blueprint

**Disclaimer: these instructions are a bit confusing, at the moment. It may be easier to take a look at the [example blueprints](https://github.com/qw3rtman/ralph/tree/master/examples).**

A blueprint is an outline of the alias being designed. Let's take a look at the blueprint for the `digitalocean` alias shown in the images above.

```
{
  "blueprint": "digitalocean {*user?} {~server?}",
```

The first part of the blueprint, `digitalocean`, is the name of the command you want to generate.

Alias parameters are defined after the first part of the blueprint. In this case, the parameters are described by `{*user?}` and `{~server?}`. Let's take a closer look at these two parameters.

- `{*user?}`
  - the opening brace (`{`) → defines a parameter
  - the asterisk (`*`) → any value is acceptable (not restricted)
  - the parameter name (`user`) → a parameter named `user`
  - the question mark (`?`) → optional value, default will be used if no argument specified
  - the closing brace (`}`) → closes the parameter definition
- `{~server?}`
  - the opening brace (`{`) → defines a parameter
  - the asterisk (`~`) → certain values are acceptable (restricted)
  - the parameter name (`server`) → a parameter named `server`
  - the question mark (`?`) → optional value, default will be used if no argument specified
  - the closing brace (`}`) → closes the parameter definition
