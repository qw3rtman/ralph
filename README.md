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

> Ralph helps you create Bash aliases that can be [**called with `sudo`**](#using-your-new-aliases), have [**parameters**](#design-a-blueprint), and print aesthetically-pleasing error messages. Ralph takes the work out of writing complex Bash aliases and provides parameter **restrictions** and **default** parameter values out-of-the-box.

### Design a *Blueprint*
![blueprint](https://cloud.githubusercontent.com/assets/1139621/7335747/8b64fe6a-eb98-11e4-818a-663748c3efdd.png)

### Ask Ralph to Work His *Magic*
![magic](https://cloud.githubusercontent.com/assets/1139621/7335748/8b71f5fc-eb98-11e4-97ca-34dbab476b68.png)

### Feel *Groovy* Using Your New Alias!
![alias](https://cloud.githubusercontent.com/assets/1139621/7335749/8b7329b8-eb98-11e4-8858-5d4ed0ab4fff.png)

## Designing a Blueprint

**Disclaimer: these instructions are a bit confusing, at the moment. It may be easier to take a look at the [example blueprints](https://github.com/qw3rtman/ralph/tree/master/examples).**

A blueprint is an outline of the alias being designed. Let's take a look at the blueprint for the `digitalocean` alias shown in the images above.

```javascript
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

```javascript
  "command": "ssh {user}@{server}",
```

This is where you define what command is executed when you call your alias.

You can use any parameters defined in the `blueprint` above in your command by enclosing the parameter name in braces, as seen in the example above.

```javascript

   "arguments": {
     "user": {
       "values": {
         "default": "root"
       }
     },
```

Since `user` is an optional parameter (has a question mark, `?`, in the blueprint declaration), a `default` value is required. In the event that no `user` is specified, the `default` value will be passed in its place.

```javascript
     "server": {
       "values": {
         "default": "198.199.97.172",
         
         "website": "198.199.97.172",
         "git": "91.876.54.321"
       },
```

Keep in mind that `server`, like `user`, is also an optional paramter, so a `default` value is required.

In addition, `server` is a restricted parameter, which only allows certain, explicitly defined values to be passed. In this case, two values are defined; meaning, only these two values are acceptable parameters.

`digitalocean website` and `digitalocean git` are acceptable; however, `digitalocean invalid` would print a generic error. This error can also be explcitly defined, as outlined below.

```javascript
       "errors": {
         "invalid": "I've never heard of {server}."
       }
```

Define an `invalid` error that will be printed if the parameter is restricted and the value provided is not acceptable.

Define an `missing` error that will be printed if the paramter is **not optional** and a value is not provided.

Similar to the `command`, parameters can be used by enclosing the parameter name in braces, as seen in the example above.

```javascript
    }
  }
}
```

Ensure your blueprint contains valid JSON!

## Calling Ralph
After following the [simple installation instructions](#installation), just run `ralph` and Ralph will take care of everything else for you.

## Using Your New Aliases
Just call them! For example, with the above example: `$ digitalocean`.

In addition, you can call them with `sudo`, **unlike classic Bash aliases**: `$ sudo digitalocean`.

## Installation
Installation is super-simple: no finicky package managers or dependencies (**other than Python**); just pure drag-and-drop.

After downloading `ralph`, simply copy it over to your `$PATH` and you're good to go.
```sh
$ wget https://github.com/qw3rtman/ralph/releases/download/v0.1.0/ralph
$ chmod +x ralph
$ mv ralph /usr/local/bin
```

If you don't have `wget` on your system, you can download `ralph` from the [releases page](https://github.com/qw3rtman/ralph/releases) and follow the above steps from the second one onward.

**Now just run `ralph` once and Ralph will take care of setting up your `~/.ralph` directory with all the default settings.**

## Configuration
All configuration for `ralph` are found in `~/.ralph/config.json`. Here, you can tell Ralph where to search for blueprint JSON files and where to place alias files after they are generated.

## Limitations
The major limitation with `ralph` is inherent in optional parameters.

In the above example (`digitalocean`), suppose you want to utilize the default value of `user` (the first paramter) by leaving it blank, `ralph` will just assume the first parameter is what the second parameter was intended to be.

```sh
$ digitalocean website
```

Here, I intended for the `user` parameter to default to the `default` value; however, the `user` parameter would be `website` and the `server` parameter would be blank, resulting in it default to the `default` value.

While I intended for the above command to result in:

```sh
$ ssh root@198.199.97.172
```

It would actually result in:

```sh
$ ssh website@198.199.97.172
```
