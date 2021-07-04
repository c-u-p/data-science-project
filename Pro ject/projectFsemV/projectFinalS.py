

import pandas as pd
import matplotlib.pyplot as plt
df_tseries_data=pd.read_csv(r'F:\College2020\SDL\SDL - Prof AMM\Pro ject\projectFsemV\t_series_p_data.csv')
df_tseries_data
plt.bar(x=df_tseries_data['Date'], height=df_tseries_data['20-Sep'])
plt.show()
