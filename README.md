Osteosarcoma detection using image processing. 

Datset- https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=52756935

Approach inspired by 
https://ieeexplore.ieee.org/document/9752602

Under the guidance of Dr. Megha Agarwal. 

Teammates- 
https://www.linkedin.com/in/shrijit-srivastav-1704301b1/


https://www.linkedin.com/in/jai-arora-op/


https://www.linkedin.com/in/aditya-roy-chowdhury-a248931b2/


Initially tried Support Vector Machine, followed by Nested SVM for multiclassification, which gave subpar results. So switched to image processing. 
During the time period of the project, CellProfier is still unavailable as a library, to import to Google Colab / Jupyter Notebook. 
Hence, pipeline for feature extraction was done on the .exe windows application. The colab file follows through next steps, from csv to the XgBoost model. 

Usage- Run the .ipynb file for XGBoost on Colab/Jupyter Notebook, and use csv files, in desired path. For SVM, download the dataset, and feed it to the model after processing. SVM model was tested on a smaller dataset to test things out, which initially failed. So runnning it is not necessary, purely a choice. 
For building the Cellprofiler Pipeline, download application from - 

[CellProfiler Download](https://cellprofiler.org/releases)

and refer to tutorial from - 

[Youtube Playlist](https://www.youtube.com/playlist?list=PLeM_d8ZXiMCP1el4oT591FQWlF2FdSfMN)

The research paper explains what masks and process are taken on the image to find the GLCM matrix. A "decent" hardware is recommended.