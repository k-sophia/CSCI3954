"""
Test driver for Program 20
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import p20


thetas = np.array([12, 13, 14, 15, 16, 17])
y_vals = np.array([12.1, 12.8, 14.9, 16.3, 17.2])
mse_losses = p20.mse_estimates(thetas,y_vals)
abs_losses = p20.mae_estimates(thetas,y_vals)
plt.scatter(thetas, mse_losses, label='MSE')
plt.scatter(thetas, abs_losses, label='MAE')
plt.title(r'Loss vs. $ \theta $ when $ \bf{y}$$= [ 12.1, 12.8, 14.9, 16.3, 17.2 ] $')
plt.xlabel(r'$ \theta $ Values')
plt.ylabel('Loss')
plt.legend()
# expected plot shown in loss_small_ex.png
plt.show()


thetas = np.arange(30)
tips_df = sns.load_dataset('tips')
tipsPercent = (tips_df['tip']/tips_df['total_bill'])*100
mse_losses = p20.mse_estimates(thetas, tipsPercent)
abs_losses = p20.mae_estimates(thetas, tipsPercent)
plt.plot(thetas, mse_losses, label='MSE')
plt.plot(thetas, abs_losses, label='MAE')
plt.title(r'Loss vs. $ \theta $ for sns tips data')
plt.xlabel(r'$ \theta $ Values')
plt.ylabel('Loss')
plt.legend()
# expected plot shown in loss_tips.png
plt.show()