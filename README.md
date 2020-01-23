# .NET injection PoC 

Repository contains code samples weaponized for use with Covenant (https://github.com/cobbr/Covenant) and donut (https://github.com/TheWover/donut).

Techniques are partially described under this writing:
https://medium.com/@ditrizna/red-team-use-case-of-open-source-weaponization-5b22b0e287a5

Injection that does not relies on RWX right permissions is located under `PAYLOAD_INJECT/inject_rw_rx.cs`.  
Delivery that uses mshta.exe instead of WebDav is located under `download_compile_and_exec.hta`.

Potential improvements:  
	* adding an execution methods to `PAYLOAD_INJECT` samples in order to launch using installutil.exe, regsvr.exe  
	* adding a persistence already in `PAYLOAD EXEC` stage
