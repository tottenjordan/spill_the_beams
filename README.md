## spill_the_beams

running pipeline with `python3 main.py`

Current error message: `AttributeError: Can't get attribute '_create_code' on <module 'dill._dill' from '/usr/local/lib/python3.7/site-packages/dill/_dill.py`

I'm not sure if packages are being installed correctly on the workers. I've tried both: (1) `'--requirements_file', 'requirements.txt'` and (2) `'--setup_file', './setup.py',` 

* In [Managing Dependencies](https://beam.apache.org/documentation/sdks/python-pipeline-dependencies/), it seems only a `requirements.txt` file is needed it the pipeline code is contained in one file? (as opposed to using something like `--setup_file /path/to/setup.py`)
* See `_create_code()` [here](https://github.com/uqfoundation/dill/blob/master/dill/_dill.py#L1170)

