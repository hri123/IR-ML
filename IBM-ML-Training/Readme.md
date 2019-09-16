# Dev Environment Setup

IDE: VSCode

Install `Anaconda Extension Pack` Extension

Opening Working Project:
File -> Add Folder to Workspace -> /Users/hrishikesh/C/git/github.com/IR-ML/IBM-ML-Training

Install:
- Ananconda: https://www.anaconda.com/distribution/ - Python 3 version - https://repo.anaconda.com/archive/Anaconda3-2019.07-MacOSX-x86_64.pkg (Note: installation takes a lot of time)
`(base) Hrishikesh-Kumar-MacBook-Pro:~ hrishikesh$ conda` conda (//anaconda3/bin/conda) command must work now

(base) Hrishikesh-Kumar-MacBook-Pro:anaconda3 hrishikesh$ //anaconda3/bin/python3 -V
Python 3.7.3


## Conda maintainence

Version:
(base) Hrishikesh-Kumar-MacBook-Pro:anaconda3 hrishikesh$ conda -V
conda 4.7.10

Update:
(base) Hrishikesh-Kumar-MacBook-Pro:anaconda3 hrishikesh$ conda update conda

Create Virtual Env
(base) Hrishikesh-Kumar-MacBook-Pro:anaconda3 hrishikesh$ conda create -p /Users/hrishikesh/C/git/github.com/IR-ML/IBM-ML-Training/env-ibm-ml-training python=3.7.3

To activate this environment, use
conda activate /Users/hrishikesh/C/git/github.com/IR-ML/IBM-ML-Training/env-ibm-ml-training
To deactivate an active environment, use
conda deactivate

Select this Virtual Env inside VSCODE
Cmd Shft P -> Python: Select Interpreter -> (select workspace) -> (select the virtual env created previously)

/Users/hrishikesh/C/git/github.com/.vscode/settings.json will have
{
    "python.pythonPath": "IR-ML/IBM-ML-Training/env-ibm-ml-training/bin/python"
}

Install Package:
conda install -p /Users/hrishikesh/C/git/github.com/IR-ML/IBM-ML-Training/env-ibm-ml-training numpy
Uninstall:
conda remove -p /Users/hrishikesh/C/git/github.com/IR-ML/IBM-ML-Training/env-ibm-ml-training numpy


## Move to other machines

When you're ready to deploy the application to other computers, you can create a requirements.txt file with the command pip freeze > requirements.txt (pip3 on macOS/Linux).

pip install -r requirements.txt (or, again, pip3 on macOS/Linux).

