"""
This module defines the model_eval funtion which can be further used to either test or validate the PyTorch
neural network model.
"""
import torch
from torch import nn
from torch.utils.data import DataLoader
from .metrics.confusion_matrix import ConfusionMatrix

def model_eval(model: nn.Module,
               dataloader: DataLoader,
               criterion: nn.Module,
               confusion_matrix: ConfusionMatrix):

    """
    Evaluate a PyTorch neural network model on a given DataLoader.

    This function is used to validate the model on a validation dataset or test it on a test dataset.
    It calculates the model's accuracy and monitors the loss by predicting labels for the input data
    and comparing them to the ground truth.

    Params:
        model (nn.Module): Any neural network model that is a subclass of torch.nn.Module to be validated.
        dataloader (DataLoader): DataLoader containing the dataset for evaluation.
                                 It provides batches of data (images and labels) for evaluation.
        criterion (nn.Module): The loss function used for calculating the loss.
        confusion_metrix (ConfusionMatrix): The confusion matrix used to calculate metrics. 
                                            The metric strategies need to be set before calling this function!

    Returns:
            - total_loss (float): The total loss on the dataset.
            - av_loss (float): The average loss per batch.
            - calculated_metrics (tuple): Metrcis calculated using the confusion matrix.
    """
    # Set the model to evaluation mode.
    model.eval()
    total_loss = 0.0
    
    # Disable gradient calculations.
    with torch.no_grad():

        # Iterate over the validation data.
        for images, labels in dataloader:
            
            # Forward pass: compute the model output for the batch.
            outputs = model(images)

            # Calculate the loss for the batch.
            loss = criterion(outputs, labels)
            total_loss += loss.item()

            # Get the index of the highest probability class for each image,
            # which represents the predicted label.
            _, predictions = torch.max(outputs, 1)

            confusion_matrix.step(ground_truth=labels,
                                  quantized_preds=predictions)

    # Calculate the average loss per each batch.
    av_loss = total_loss / len(dataloader)

    # Calculate the metrics using the confusion matrix
    calculated_metrics = tuple(confusion_matrix.calculate_metric(as_percentage=True, as_dict=False))

    return total_loss, av_loss, calculated_metrics
