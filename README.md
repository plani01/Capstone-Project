# About this repository: ML- Semester 2 of Senior Capstone Project
This was work completed during the second semester of my senior design project. I had sole responsibility to create a robust ML model to  
use for an autonomous trash pickup robot. Half of the first semesester was devoted to supplemntal CPE labs unrelated to our project. At the  
end of that semester I was able to train and integrate a YOLOv5 ML model.  
  
In Design 2 I wanted to learn more about ML so I attempted to create a custom CNN architecture. Before I worked  on a CNN model, I experimented
with SVM type models, but discovered that they were infeasible due to model size. A majority of the time after was spent adjusting my training
data and experimenting with image data augmentation. I learned how to create healthy variance in my data set and how to properly augment the data.
However, my time was running out in the semester and my architecture was still too basic. In the end, I quickly trained another Yolo model to use 
for the final demo.  
  
The "Models Training Folder" shows multiple variations and progress of the models. "Preprocesing" includes a data collection and data augmentation scripts.  
"Models testing" includes scripts that perform perdiction on the different models. One script also measures the latency between predictions.  
  
Below is a video showcasing the final build.  

[![Watch the video](https://img.youtube.com/vi/<VIDEO_ID>/hqdefault.jpg)]([https://www.youtube.com/embed/<VIDEO_ID>](https://www.youtube.com/watch?v=6qF6f0tlELE))

[<img src="https://img.youtube.com/vi/6qF6f0tlELE/hqdefault.jpg" width="400" height="300"
/>](https://www.youtube.com/watch?v=6qF6f0tlELE)


 
**Steps to Compile the Code:**  
1.) Download the python virtual environment manager called Anaconda. If desired, Miniconda can also be used if disk space is a concern.   
Anaconda: https://www.anaconda.com/download/  
Miniconda: https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html  

2.) Clone this repo into a directory of your choosing. 

3.) Request and download my training images   

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

10.) Change the absolute file paths in the to the training image files. The variables for file paths are usually located in the fourth jupyter cell.  

11.) If the first cell (library loading) sucessfully runs with errors. All further cells can be run and edits can be made. 

**End of Steps**  



