# Separate Node.js file producer

This deliberately limited synthetic example regenerates a message ID, changes decimal
lexical scale, reorders remittance values and changes the namespace prefix. The contract
allows these changes. It is not a production XML adapter, and accepts only the original
six bundled synthetic sources. Do not adapt it to real institution files.

Run it yourself, outside MessageBench:

```sh
node examples/file-handoff/demo-adapter.mjs /tmp/my-messagebench-outputs
mkdir /tmp/my-messagebench-report
messagebench suite corpus/gate1-index.json --outputs /tmp/my-messagebench-outputs \
  --out /tmp/my-messagebench-report
```

Use new directories on each run; existing files are not overwritten. Node.js is only an
optional demonstration dependency, never a MessageBench runtime dependency. The toolkit
cannot invoke this script. This demonstrates the language-neutral file boundary; it is
not independent external review or real-world adoption.
