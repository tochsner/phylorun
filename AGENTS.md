# PhyloData Python Library - Agent Guidelines

## Development Guidelines

### Code Style & Standards

- **Python 3.10+**: Use modern Python features and syntax
- **Pytest**: Testing framework
- **Click**: CLI interface framework

## Best Practices for Agents

### When Working on This Project

- **Understand the Domain**: Familiarize yourself with the terminology
- **Use Modern Python**: Leverage Python 3.10+ features like pattern matching and improved type hints
- **Type Everything**: Add comprehensive type hints to all functions and classes
- **Docstrings**: Add docstrings for everything but internal provate functions. Arguments need only be described in user-facing methods
- **Modular Design**: Think about software design. Design components in a modular but concise way
- **Handle Errors Gracefully**: Use custom exceptions and proper error messages
- **Use Path Objects**: Prefer `pathlib.Path` over string paths
- **Top-down approach**: Have the main functions first, followed by smaller helper functions

### Code Quality Standards

- **No Unnecessary Comments**: Use descriptive variable names and docstrings instead
- **Consistent Style**: Follow existing code patterns and naming conventions
- **Small, Focused Changes**: Break down large changes into manageable tasks

## Engine Documentation

BEAST X CLI documentation:

```
Usage: beast [-verbose] [-warnings] [-strict] [-window] [-options] [-working] [-seed] [-prefix <PREFIX>] [-overwrite] [-errors <i>] [-threads <i>] [-fail_threads] [-ignore_versions] [-java] [-tests] [-threshold <r>] [-show_operators] [-adaptation_off] [-adaptation_target <r>] [-pattern_compression <off|unique|ambiguous_constant|ambiguous_all>] [-ambiguous_threshold <r>] [-beagle] [-beagle_info] [-beagle_auto] [-beagle_order <order>] [-beagle_instances <i>] [-beagle_multipartition <auto|on|off>] [-beagle_CPU] [-beagle_GPU] [-beagle_SSE] [-beagle_SSE_off] [-beagle_threading_off] [-beagle_threads <i>] [-beagle_cuda] [-beagle_opencl] [-beagle_single] [-beagle_double] [-beagle_async] [-beagle_low_memory] [-beagle_extra_buffer_count <buffer_count>] [-beagle_scaling <default|dynamic|delayed|always|none>] [-beagle_delay_scaling_off] [-beagle_rescale] [-mpi] [-particles <FOLDER>] [-mc3_chains <i>] [-mc3_delta <r>] [-mc3_temperatures] [-mc3_swap <i>] [-mc3_scheme <NAME>] [-load_state <FILENAME>] [-save_stem <FILENAME>] [-save_at] [-save_time <HH:mm:ss>] [-save_every] [-save_state <FILENAME>] [-full_checkpoint_precision] [-force_resume] [-citations_file <FILENAME>] [-citations_off] [-plugins_dir <FILENAME>] [-version] [-help] [<input-file-name>]
    -verbose Give verbose XML parsing messages
    -warnings Show warning messages about BEAST XML file
    -strict Fail on non-conforming BEAST XML file
    -window Provide a console window
    -options Display an options dialog
    -working Change working directory to input file's directory
    -seed Specify a random number generator seed
    -prefix Specify a prefix for all output log filenames
    -overwrite Allow overwriting of log files
    -errors Specify maximum number of numerical errors before stopping
    -threads The maximum number of computational threads to use (default auto)
    -fail_threads Exit with error on uncaught exception in thread
    -ignore_versions Ignore mismatches between XML and BEAST versions
    -java Use Java only, no native implementations
    -tests The number of full evaluation tests to perform (default 1000)
    -threshold Full evaluation test threshold (default 0.1)
    -show_operators Print transition kernel performance to file
    -adaptation_off Don't adapt operator sizes
    -adaptation_target Target acceptance rate for adaptive operators (default 0.234)
    -pattern_compression Site pattern compression mode - unique | ambiguous_constant | ambiguous_all (default unique)
    -ambiguous_threshold Maximum proportion of ambiguous characters to allow compression (default 0.25)
    -beagle Use BEAGLE library if available (default on)
    -beagle_info BEAGLE: show information on available resources
    -beagle_auto BEAGLE: automatically select fastest resource for analysis
    -beagle_order BEAGLE: set order of resource use
    -beagle_instances BEAGLE: divide site patterns amongst instances
    -beagle_multipartition BEAGLE: use multipartition extensions if available (default auto)
    -beagle_CPU BEAGLE: use CPU instance
    -beagle_GPU BEAGLE: use GPU instance if available
    -beagle_SSE BEAGLE: use SSE extensions if available
    -beagle_SSE_off BEAGLE: turn off use of SSE extensions
    -beagle_threading_off BEAGLE: turn off multi-threading for a CPU instance
    -beagle_threads BEAGLE: manually set number of threads per CPU instance (default auto)
    -beagle_cuda BEAGLE: use CUDA parallization if available
    -beagle_opencl BEAGLE: use OpenCL parallization if available
    -beagle_single BEAGLE: use single precision if available
    -beagle_double BEAGLE: use double precision if available
    -beagle_async BEAGLE: use asynchronous kernels if available
    -beagle_low_memory BEAGLE: use lower memory pre-order traversal kernels
    -beagle_extra_buffer_count BEAGLE: reserve extra transition matrix buffers for convolutions
    -beagle_scaling BEAGLE: specify scaling scheme to use
    -beagle_delay_scaling_off BEAGLE: don't wait until underflow for scaling option
    -beagle_rescale BEAGLE: frequency of rescaling (dynamic scaling only)
    -mpi Use MPI rank to label output
    -particles Specify a folder of particle start states
    -mc3_chains number of chains
    -mc3_delta temperature increment parameter
    -mc3_temperatures a comma-separated list of the hot chain temperatures
    -mc3_swap frequency at which chains temperatures will be swapped
    -mc3_scheme Specify parallel tempering swap scheme
    -load_state Specify a filename to load a saved state from
    -save_stem Specify a stem for the filenames to save states to
    -save_at Specify a state at which to save a state file
    -save_time Specify a length of time after which to save a state file
    -save_every Specify a frequency to save the state file
    -save_state Specify a filename to save state to
    -full_checkpoint_precision Use hex-encoded doubles in checkpoint files
    -force_resume Force resuming from a saved state
    -citations_file Specify a filename to write a citation list to
    -citations_off Turn off writing citations to file
    -plugins_dir Specify a directory to load plugins from, multiple can be separated with ':' 
    -version Print the version and credits and stop
    -help Print this information and stop

  Example: beast test.xml
  Example: beast -window test.xml
  Example: beast -help
```

BEAST 2 CLI documentation: https://www.beast2.org/2019/09/26/command-line-tricks.html and https://www.beast2.org/2021/03/31/command-line-options.html

RevBayes CLI documentation: 

````
Options:
  -h [ --help ]         Show information on flags.
  -v [ --version ]      Show version and exit.
  -b [ --batch ]        Run in batch mode.
  -j [ --jupyter ]      Run in jupyter mode.
  --args arg            Command line arguments to initialize RevBayes 
                        variables.
  --cmd arg             Script and command line arguments to initialize 
                        RevBayes variables.
  --file arg            File(s) to source.
  --setOption arg       Set an option key=value. See ?setOption for the list of
                        available keys and their associated values.
```
