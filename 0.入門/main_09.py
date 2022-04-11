import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

#st.write('DataFrame')
#df = pd.DataFrame(
#    np.random.rand(100,2)/[50,50] + [35.69,139.70],
#    columns=['lat','lon']
#    '1列目': [1,2,3,4],
#    '2列目': [10,20,30,40]
#)
#st.dataframe(df.style.highlight_max(axis=0))
#st.table(df.style.highlight_max(axis=0))
#st.area_chart(df)
#st.map(df)

st.write('Display Image')
img = Image.open('thumbnail_yaruki_aru_suit.jpg')
st.image(img,caption='irasutoya',use_column_width=True)

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""
