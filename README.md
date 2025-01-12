## 1. Environment Setup

Before starting with the dataset preparation or running any scripts, make sure to set up the project environment.

1. **Create the Conda environment:**
   Ensure that you have Conda installed (via Anaconda or Miniconda). Then, run the following command to create the environment:
   ```bash
   conda env create -f environment.yml
   ```

2. **Activate the environment:**
   Once the environment is created, activate it with:
   ```bash
   conda activate xray_classification
   ```

3. **Customize the environment name (optional):**
   By default, the environment is named `xray_classification`, as defined in the `environment.yml` file. If you prefer a different name, you can edit the `name` field in the file before running the environment creation command. For example:
   ```yaml
   name: your_custom_name
   ```
   After editing, run:
   ```bash
   conda env create -f environment.yml
   conda activate your_custom_name
   ```

4. **Verify the installation:**
   To ensure all dependencies were installed correctly, you can list the installed packages:
   ```bash
   conda list
   ```
   Additionally, confirm that the PyTorch and related libraries (e.g., `torch`, `torchvision`, `torchaudio`) are working as expected:
   ```bash
   python -c "import torch; print(torch.__version__)"
   ```

---

## 2. Downloading CheXpert dataset and preparing its file structure

- Download the dataset from the official website. [LINK](https://stanfordaimi.azurewebsites.net/datasets/8cbd9ed4-2eb9-4565-affc-111cf4f7ebe2)
- Unzip all the files listed below:
	- `CheXpert-v1.0 batch 1 (validate & csv).zip`
	- `CheXpert-v1.0 batch 2 (train 1).zip`
	- `CheXpert-v1.0 batch 3 (train 2).zip`
	- `CheXpert-v1.0 batch 4 (train 3).zip`
	
- Move all the `patientXXXXX` folders (XXXXX stands for the patient number) from the `CheXpert-v1.0 batch 1 (validate & csv)/valid` directory into the new `valid_data` folder within the CheXpert root directory.

- Move both the `train.csv` and `valid.csv` files from the `CheXpert-v1.0 batch 1 (validate & csv)` to the CheXpert root directory

- Remove the empty `CheXpert-v1.0 batch 1 (validate & csv)` folder

- Move all the `patientXXXXX` folders (XXXXX stands for the patient number) from all the unzipped `CheXpert-v1.0 batch x (train y)` folders into the new `train_data` folder within the CheXpert root directory.

- Remove all the empty `CheXpert-v1.0 batch x (train y)` folders.
- Remove all the other unnecessary files not mentioned above (mostly CSVs and other models stats files). Leave the `README.md` if you want. NOTE: Removing the zip files mentioned above is not recommended! If you mess anything with the file structure, fixing it would involve downloading the whole dataset again. Keep the zip files to save the time in case of the file moving mistake.

- At this stage, the file structure should be as follows::
	- `CheXpert_root_directory` (you can name it as you wish)
		- `train_data`
			- `patient00001`
			- `patient00002`
			- `...`
			- `patient64540`
		- `valid_data`
			- `patient6541`
			- `patient6542`
			- `...`
			- `patient64740`
		- `train.csv` (file containing all the training images information and the labels)
		- `valid.csv` (file containing all the validation images information and the labels)
		- `CheXpert-v1.0 batch 1 (validate & csv).zip`
		- `CheXpert-v1.0 batch 2 (train 1).zip`
		- `CheXpert-v1.0 batch 3 (train 2).zip`
		- `CheXpert-v1.0 batch 4 (train 3).zip`
		- `README.md`(optional)

## 3. To-Do in README

-  **Code structure and module descriptions:** 

	Include a detailed explanation of the project's folder structure, code modules, and naming conventions used throughout the project.
- **Insights from exploratory data analysis (EDA):**
  
	Summarize key findings from EDA of the CheXpert dataset, particularly those that influenced decisions for splitting the dataset into training and testing sets. Note: the validation set is provided separately in the CheXpert dataset.
- **Preparing CSV files for training, testing, and validation:** 
  
	Provide a step-by-step guide on how the dataset's CSV files (`train.csv`, `valid.csv`) are prepared, and how the dataset is split into training and testing sets. This should also cover examples of resulting CSV structure or content.
- **Model training, testing, and validation using provided CLI:** 
  
  	Command-line example(s) for running the training, testing and validation.
- **Predicting image classes using provided CLI and both trained and validated model:**
  
  	Command-line example(s) for running the prediction
  
## License
MIT License

Copyright (c) 2025 Jan Świderski

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
## Responsibility disclaimer
Author of the script do not take any responsibility for any losses made by script and its usage. User uses the script on own responsibility.