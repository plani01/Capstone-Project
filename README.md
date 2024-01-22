# ML-Design2
This is the repo for Machine learning code written during Design2. More organization and some different ideas compared to the Design1 repo. 

## Alpha Build : 

**Steps to Compile my Code:**  
1.) Download the python virtual environment manager called Anaconda. If desired, Miniconda can also be used if disk space is a concern.   
Anaconda: https://www.anaconda.com/download/  
Miniconda: https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html  

2.) Clone this repo into a directory of your choosing. 

3.) From the Design 1 repo "Machine Learning" download only the pictures. These pictures are used for training the ML model. Some of the same pictures are used to test the model's prediction as well.   

4.) Anaconda should come with a program called Anaconda Navigator and Anaconda Prompt. Anaconda Navigator is the GUI version of the Anaonda Prompt Terminal.  
Open Anaconda Prompt

5.) Create and load a copy of my python virtual environment by running the command:  
conda create --name myenv --file spec-file.txt  
Note: The command must be run where the repo is cloned (or give a path to the spec-file.txt). Also, change <myenv> to a name of your choosing.  

6.) Launch the virtual environment:  
conda activate \<your environment name>

7.) Launch the jupyter notebook with the command:  
jupyter notebook  

8.) Jupyter notebook will launch a local directory viewer in your browser. Navigate to the directory where the repo was cloned.  

9.) Click on any file to view them. Files with extension .ipynb are jupyter notebook python executables. They have individual cells that can be ran, similar to Matlab.  

10.) Change the absolute file pats in the "Training using SVM" and "Predition using SVM" files. The variables for file paths are located in the fourth jupyter cell.  

11.) If the first cell (library loading) sucessfully runs with errors. All further cells can be run and edits can be made. 

**End of Steps**  



