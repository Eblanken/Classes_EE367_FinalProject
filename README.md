This repository is maintained by Erick Blankenberg (eblanken@stanford.edu, erick.blankenberg@gmail.com) and Scott Blankenberg (sblanken@stanford.edu). If you have any questions, do not hesitate to reach out to us.

This repository is structured as follows:

- Final_Project_EvaluationScript.ipynb: Main code file, a Jupyter notebook which downloads the datasets, allows the user to run each of the disparity algorithms, and generates documentation of results
- Algorithms: This folder contains subfolders which contain code to each of the algorithms under consideration. Note that you will need to create additional cells in the Jupyter notebook to evaluate new algorithms
- Data: Created by the Jupyter Notebook which populates the folder with datasets including stereo pairs, camera calibration files, and ground truth disparities. Additional data can be added as per the instructions in the notebook. When the notebook is run all datasets in this folder are automatically cataloged evaluated with the disparity algorithms.
- Output: Created by the Jupyter Notebook which populates the folder with disparity outputs and runtimes for each of the datasets and algorithms.
- Utils: Folder with some helper functions used in the Jupyter Notebook

Before running the script you need to have the proper Python libraries installed. 
This can be accomplished by installing and activating the provided environment file as follows.
Navigate to the "Utils" folder in your terminal and type
"conda env create -f stereoEnviron.yml". This will install all of the libraries
required to run the algorithms under consideration. Note that some algorithms require additional files which are
downloaded by corresponding cells at the beginning of the Jupyter Notebook. Then activate the environment
after packages are installed by typing the command "conda activate stereoEnviron".
You then need to add the kernel to those accessable to Jupiter Notebooks with the command 
"python -m ipykernel install --user --name=stereoEnviron". Start the Jupyter notebook with the command
"Jupyter Notebook" while in the base directory of the project. Now open the evaluation script. Make sure 
to select "stereoEnviron" from the kernel list. Run the cells in order. Note that some of them, especially 
those that import image data, can take a very long time.

If you run into issues, please reach out to us directly.