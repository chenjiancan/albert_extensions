# albert_extensions
albert launcher extension scripts

# albert extension dev
* albert 
https://albertlauncher.github.io
* doc
https://albertlauncher.github.io/docs/extending/external/

## how it works
* albert scan following paths to find extensions

* a extension is a executable script wrote in any script language you like, eg, python, shell ...
  the extension script would be involved one or more times when user a type in the input box
  
* communication between albert and a extension
  It's like a c/s model, albert request and extension response accordingly
  * albert request use Environment Variable to pass infomation to extension
  * extension response a json string through the standard output stream (stdout). 
  
  
* what should we write in the extension script
  albert usg Environment Variable to pass infomation to extension
  "METADATA" "NAME" "INITIALIZE"  "FINALIZE"  "SETUPSESSION"  "SETUPSESSION"  "TEARDOWNSESSION" "QUERY"  "COPYTOCLIPBOARD"
  
  METADATA : albert ask extension about basic info, extensoin should return a json like:
```
    metadata="""{
      "iid":"org.albert.extension.external/v2.0",
      "name":"ls",
      "version":"1.0",
      "author":"raiz",
      "dependencies":[],
      "trigger":"ls"
    }"""
    print(metadata)
```    
  where trigger is what shortcut we type in albert input box to identify the extension
  
  QUERY : after usre type "trigger", every time the input changge, a query command would be pass to extension that are relative
  extension should return a json string like:

```
{
 "items": [{
   "id":"extension.wide.unique.id",
   "name":"An Item",
   "description":"Nice description.",
   "icon":"/path/to/icon",
   "actions":[
     {
       "name":"Action name 1",
       "command":"program",
       "arguments":["-a", "-b"]
     },
     {
       "name":"Action name 2",
       "command":"program2",
       "arguments":["-C", "-D"]
     }]
 }],
 "variables": {
   "some_var":"variable",
   "some_other_var":"cool state"
 }
}
```
  where items are what would albert show below input box and variables save state between the executions the plugin.
  where actions is a list show when user hit TAB.
  command stands for a program to be executed where user hit ENTER

  
