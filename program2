{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "10c73bb0-4950-464b-93d6-8a08bf61030a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "a726e647-6e48-4277-800b-738a0280c2e9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "C:\\Users\\CSD\n"
     ]
    }
   ],
   "source": [
    "!cd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "0e4fb797-e2ef-420e-9cbd-7faea0bae4bc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " Volume in drive C has no label.\n",
      " Volume Serial Number is C4C7-FE0A\n",
      "\n",
      " Directory of C:\\Users\\CSD\n",
      "\n",
      "16-05-2024  11:56             1,700 mtcars.csv\n",
      "               1 File(s)          1,700 bytes\n",
      "               0 Dir(s)  175,288,176,640 bytes free\n"
     ]
    }
   ],
   "source": [
    "!dir mtc*\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "f8773b7d-89d3-4e65-83b3-340aa8e55446",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " Volume in drive C has no label.\n",
      " Volume Serial Number is C4C7-FE0A\n",
      "\n",
      " Directory of C:\\Users\\CSD\n",
      "\n",
      "16-05-2024  13:05    <DIR>          .\n",
      "16-05-2024  13:05    <DIR>          ..\n",
      "30-04-2024  13:50    <DIR>          .anaconda\n",
      "30-04-2024  15:13    <DIR>          .conda\n",
      "30-04-2024  13:50                25 .condarc\n",
      "30-04-2024  13:50    <DIR>          .continuum\n",
      "16-05-2024  12:17    <DIR>          .ipynb_checkpoints\n",
      "30-04-2024  13:54    <DIR>          .ipython\n",
      "10-04-2024  14:05    <DIR>          .ivy2\n",
      "10-04-2024  14:05    <DIR>          .jdks\n",
      "07-05-2024  13:48    <DIR>          .jupyter\n",
      "16-05-2024  13:05    <DIR>          .matplotlib\n",
      "15-05-2024  16:13    <DIR>          .VirtualBox\n",
      "07-05-2024  10:06    <DIR>          .vscode\n",
      "19-04-2024  10:05    <DIR>          3D Objects\n",
      "30-04-2024  13:49    <DIR>          anaconda3\n",
      "19-04-2024  10:05    <DIR>          Contacts\n",
      "15-05-2024  16:15    <DIR>          Desktop\n",
      "30-04-2024  13:49    <DIR>          Documents\n",
      "16-05-2024  11:55    <DIR>          Downloads\n",
      "19-04-2024  10:05    <DIR>          Favorites\n",
      "09-05-2024  13:44    <DIR>          IdeaProjects\n",
      "19-04-2024  10:05    <DIR>          Links\n",
      "16-05-2024  11:56             1,700 mtcars.csv\n",
      "19-04-2024  10:05    <DIR>          Music\n",
      "09-04-2024  00:57    <DIR>          OneDrive\n",
      "19-04-2024  10:05    <DIR>          Pictures\n",
      "16-05-2024  13:04            24,302 program2.ipynb\n",
      "19-04-2024  10:05    <DIR>          Saved Games\n",
      "19-04-2024  10:05    <DIR>          Searches\n",
      "30-04-2024  15:09             4,681 Untitled.ipynb\n",
      "30-04-2024  13:54                21 untitled.py\n",
      "07-05-2024  14:51             3,938 Untitled1.ipynb\n",
      "13-05-2024  16:00            10,008 Untitled2.ipynb\n",
      "14-05-2024  14:44            12,886 Untitled3.ipynb\n",
      "19-04-2024  10:05    <DIR>          Videos\n",
      "               8 File(s)         57,561 bytes\n",
      "              28 Dir(s)  175,288,176,640 bytes free\n"
     ]
    }
   ],
   "source": [
    "!dir"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "e6572fe4-a954-4c35-a14a-e95431a43b94",
   "metadata": {},
   "outputs": [],
   "source": [
    "mtcars=pd.read_csv(\"mtcars.csv\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "e607374d-17b4-4e7e-8e3e-1a87441fbc86",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>model</th>\n",
       "      <th>mpg</th>\n",
       "      <th>cyl</th>\n",
       "      <th>disp</th>\n",
       "      <th>hp</th>\n",
       "      <th>drat</th>\n",
       "      <th>wt</th>\n",
       "      <th>qsec</th>\n",
       "      <th>vs</th>\n",
       "      <th>am</th>\n",
       "      <th>gear</th>\n",
       "      <th>carb</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Mazda RX4</td>\n",
       "      <td>21.0</td>\n",
       "      <td>6</td>\n",
       "      <td>160.0</td>\n",
       "      <td>110</td>\n",
       "      <td>3.90</td>\n",
       "      <td>2.620</td>\n",
       "      <td>16.46</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Mazda RX4 Wag</td>\n",
       "      <td>21.0</td>\n",
       "      <td>6</td>\n",
       "      <td>160.0</td>\n",
       "      <td>110</td>\n",
       "      <td>3.90</td>\n",
       "      <td>2.875</td>\n",
       "      <td>17.02</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Datsun 710</td>\n",
       "      <td>22.8</td>\n",
       "      <td>4</td>\n",
       "      <td>108.0</td>\n",
       "      <td>93</td>\n",
       "      <td>3.85</td>\n",
       "      <td>2.320</td>\n",
       "      <td>18.61</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           model   mpg  cyl   disp   hp  drat     wt   qsec  vs  am  gear  \\\n",
       "0      Mazda RX4  21.0    6  160.0  110  3.90  2.620  16.46   0   1     4   \n",
       "1  Mazda RX4 Wag  21.0    6  160.0  110  3.90  2.875  17.02   0   1     4   \n",
       "2     Datsun 710  22.8    4  108.0   93  3.85  2.320  18.61   1   1     4   \n",
       "\n",
       "   carb  \n",
       "0     4  \n",
       "1     4  \n",
       "2     1  "
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mtcars.head(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "6603c4b9-79e7-48d0-ba11-a963d54e6ab6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 32 entries, 0 to 31\n",
      "Data columns (total 12 columns):\n",
      " #   Column  Non-Null Count  Dtype  \n",
      "---  ------  --------------  -----  \n",
      " 0   model   32 non-null     object \n",
      " 1   mpg     32 non-null     float64\n",
      " 2   cyl     32 non-null     int64  \n",
      " 3   disp    32 non-null     float64\n",
      " 4   hp      32 non-null     int64  \n",
      " 5   drat    32 non-null     float64\n",
      " 6   wt      32 non-null     float64\n",
      " 7   qsec    32 non-null     float64\n",
      " 8   vs      32 non-null     int64  \n",
      " 9   am      32 non-null     int64  \n",
      " 10  gear    32 non-null     int64  \n",
      " 11  carb    32 non-null     int64  \n",
      "dtypes: float64(5), int64(6), object(1)\n",
      "memory usage: 3.1+ KB\n"
     ]
    }
   ],
   "source": [
    "mtcars.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "3fdb9369-2acd-4c5b-adbb-aebbf5f138ef",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>model</th>\n",
       "      <th>mpg</th>\n",
       "      <th>cyl</th>\n",
       "      <th>disp</th>\n",
       "      <th>hp</th>\n",
       "      <th>drat</th>\n",
       "      <th>wt</th>\n",
       "      <th>qsec</th>\n",
       "      <th>vs</th>\n",
       "      <th>am</th>\n",
       "      <th>gear</th>\n",
       "      <th>carb</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>27</th>\n",
       "      <td>Lotus Europa</td>\n",
       "      <td>30.4</td>\n",
       "      <td>4</td>\n",
       "      <td>95.1</td>\n",
       "      <td>113</td>\n",
       "      <td>3.77</td>\n",
       "      <td>1.513</td>\n",
       "      <td>16.9</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>28</th>\n",
       "      <td>Ford Pantera L</td>\n",
       "      <td>15.8</td>\n",
       "      <td>8</td>\n",
       "      <td>351.0</td>\n",
       "      <td>264</td>\n",
       "      <td>4.22</td>\n",
       "      <td>3.170</td>\n",
       "      <td>14.5</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>29</th>\n",
       "      <td>Ferrari Dino</td>\n",
       "      <td>19.7</td>\n",
       "      <td>6</td>\n",
       "      <td>145.0</td>\n",
       "      <td>175</td>\n",
       "      <td>3.62</td>\n",
       "      <td>2.770</td>\n",
       "      <td>15.5</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>30</th>\n",
       "      <td>Maserati Bora</td>\n",
       "      <td>15.0</td>\n",
       "      <td>8</td>\n",
       "      <td>301.0</td>\n",
       "      <td>335</td>\n",
       "      <td>3.54</td>\n",
       "      <td>3.570</td>\n",
       "      <td>14.6</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>31</th>\n",
       "      <td>Volvo 142E</td>\n",
       "      <td>21.4</td>\n",
       "      <td>4</td>\n",
       "      <td>121.0</td>\n",
       "      <td>109</td>\n",
       "      <td>4.11</td>\n",
       "      <td>2.780</td>\n",
       "      <td>18.6</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             model   mpg  cyl   disp   hp  drat     wt  qsec  vs  am  gear  \\\n",
       "27    Lotus Europa  30.4    4   95.1  113  3.77  1.513  16.9   1   1     5   \n",
       "28  Ford Pantera L  15.8    8  351.0  264  4.22  3.170  14.5   0   1     5   \n",
       "29    Ferrari Dino  19.7    6  145.0  175  3.62  2.770  15.5   0   1     5   \n",
       "30   Maserati Bora  15.0    8  301.0  335  3.54  3.570  14.6   0   1     5   \n",
       "31      Volvo 142E  21.4    4  121.0  109  4.11  2.780  18.6   1   1     4   \n",
       "\n",
       "    carb  \n",
       "27     2  \n",
       "28     4  \n",
       "29     6  \n",
       "30     8  \n",
       "31     2  "
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mtcars.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "797567dc-07cd-4df1-acab-057e5e8eae6d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(32, 12)"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mtcars.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "8a451789-2ba6-489a-b9cc-9c6454b3be07",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 32 entries, 0 to 31\n",
      "Data columns (total 12 columns):\n",
      " #   Column  Non-Null Count  Dtype  \n",
      "---  ------  --------------  -----  \n",
      " 0   model   32 non-null     object \n",
      " 1   mpg     32 non-null     float64\n",
      " 2   cyl     32 non-null     int64  \n",
      " 3   disp    32 non-null     float64\n",
      " 4   hp      32 non-null     int64  \n",
      " 5   drat    32 non-null     float64\n",
      " 6   wt      32 non-null     float64\n",
      " 7   qsec    32 non-null     float64\n",
      " 8   vs      32 non-null     int64  \n",
      " 9   am      32 non-null     int64  \n",
      " 10  gear    32 non-null     int64  \n",
      " 11  carb    32 non-null     int64  \n",
      "dtypes: float64(5), int64(6), object(1)\n",
      "memory usage: 3.1+ KB\n"
     ]
    }
   ],
   "source": [
    "mtcars.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "0dc7b879-1c48-40e6-a079-69c2ed58840a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>mpg</th>\n",
       "      <th>cyl</th>\n",
       "      <th>disp</th>\n",
       "      <th>hp</th>\n",
       "      <th>drat</th>\n",
       "      <th>wt</th>\n",
       "      <th>qsec</th>\n",
       "      <th>vs</th>\n",
       "      <th>am</th>\n",
       "      <th>gear</th>\n",
       "      <th>carb</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>32.000000</td>\n",
       "      <td>32.000000</td>\n",
       "      <td>32.000000</td>\n",
       "      <td>32.000000</td>\n",
       "      <td>32.000000</td>\n",
       "      <td>32.000000</td>\n",
       "      <td>32.000000</td>\n",
       "      <td>32.000000</td>\n",
       "      <td>32.000000</td>\n",
       "      <td>32.000000</td>\n",
       "      <td>32.0000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>20.090625</td>\n",
       "      <td>6.187500</td>\n",
       "      <td>230.721875</td>\n",
       "      <td>146.687500</td>\n",
       "      <td>3.596563</td>\n",
       "      <td>3.217250</td>\n",
       "      <td>17.848750</td>\n",
       "      <td>0.437500</td>\n",
       "      <td>0.406250</td>\n",
       "      <td>3.687500</td>\n",
       "      <td>2.8125</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>6.026948</td>\n",
       "      <td>1.785922</td>\n",
       "      <td>123.938694</td>\n",
       "      <td>68.562868</td>\n",
       "      <td>0.534679</td>\n",
       "      <td>0.978457</td>\n",
       "      <td>1.786943</td>\n",
       "      <td>0.504016</td>\n",
       "      <td>0.498991</td>\n",
       "      <td>0.737804</td>\n",
       "      <td>1.6152</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>10.400000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>71.100000</td>\n",
       "      <td>52.000000</td>\n",
       "      <td>2.760000</td>\n",
       "      <td>1.513000</td>\n",
       "      <td>14.500000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>1.0000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>15.425000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>120.825000</td>\n",
       "      <td>96.500000</td>\n",
       "      <td>3.080000</td>\n",
       "      <td>2.581250</td>\n",
       "      <td>16.892500</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>2.0000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>19.200000</td>\n",
       "      <td>6.000000</td>\n",
       "      <td>196.300000</td>\n",
       "      <td>123.000000</td>\n",
       "      <td>3.695000</td>\n",
       "      <td>3.325000</td>\n",
       "      <td>17.710000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>2.0000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>22.800000</td>\n",
       "      <td>8.000000</td>\n",
       "      <td>326.000000</td>\n",
       "      <td>180.000000</td>\n",
       "      <td>3.920000</td>\n",
       "      <td>3.610000</td>\n",
       "      <td>18.900000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>4.0000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>33.900000</td>\n",
       "      <td>8.000000</td>\n",
       "      <td>472.000000</td>\n",
       "      <td>335.000000</td>\n",
       "      <td>4.930000</td>\n",
       "      <td>5.424000</td>\n",
       "      <td>22.900000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>8.0000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             mpg        cyl        disp          hp       drat         wt  \\\n",
       "count  32.000000  32.000000   32.000000   32.000000  32.000000  32.000000   \n",
       "mean   20.090625   6.187500  230.721875  146.687500   3.596563   3.217250   \n",
       "std     6.026948   1.785922  123.938694   68.562868   0.534679   0.978457   \n",
       "min    10.400000   4.000000   71.100000   52.000000   2.760000   1.513000   \n",
       "25%    15.425000   4.000000  120.825000   96.500000   3.080000   2.581250   \n",
       "50%    19.200000   6.000000  196.300000  123.000000   3.695000   3.325000   \n",
       "75%    22.800000   8.000000  326.000000  180.000000   3.920000   3.610000   \n",
       "max    33.900000   8.000000  472.000000  335.000000   4.930000   5.424000   \n",
       "\n",
       "            qsec         vs         am       gear     carb  \n",
       "count  32.000000  32.000000  32.000000  32.000000  32.0000  \n",
       "mean   17.848750   0.437500   0.406250   3.687500   2.8125  \n",
       "std     1.786943   0.504016   0.498991   0.737804   1.6152  \n",
       "min    14.500000   0.000000   0.000000   3.000000   1.0000  \n",
       "25%    16.892500   0.000000   0.000000   3.000000   2.0000  \n",
       "50%    17.710000   0.000000   0.000000   4.000000   2.0000  \n",
       "75%    18.900000   1.000000   1.000000   4.000000   4.0000  \n",
       "max    22.900000   1.000000   1.000000   5.000000   8.0000  "
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mtcars.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "381c3b5e-7abc-4e2d-afe1-ae37572d0d53",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "model     object\n",
       "mpg      float64\n",
       "cyl        int64\n",
       "disp     float64\n",
       "hp         int64\n",
       "drat     float64\n",
       "wt       float64\n",
       "qsec     float64\n",
       "vs         int64\n",
       "am         int64\n",
       "gear       int64\n",
       "carb       int64\n",
       "dtype: object"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mtcars.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "2f7531d4-8359-433c-bb42-f7f27b6692e0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['model', 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am',\n",
       "       'gear', 'carb'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mtcars.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "a4eb1ec2-cfd8-4bb6-a740-73f28bc244aa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAjEAAAHFCAYAAAADhKhmAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjguMCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy81sbWrAAAACXBIWXMAAA9hAAAPYQGoP6dpAAA8OklEQVR4nO3deVxU9f7H8fe4MIACrggqoKWgpqaGmWmJmppbZpvlhlvlVhZ1M7fUNDW92XLropWSVmpZmplLmgtqSm6pLURaKK4pmoILk8L5/dFlfo0swggcj76ej8c89HzPd875zJcv8OacM2dshmEYAgAAsJhiZhcAAADgDkIMAACwJEIMAACwJEIMAACwJEIMAACwJEIMAACwJEIMAACwJEIMAACwJEIMAACwJEIMCtwHH3wgm82m7du3Z7u+U6dOqlatmktbtWrV1KdPn3ztZ/PmzRo3bpxOnz7tXqE3oE8++US33HKLvLy8ZLPZtGvXrmz7rV+/XjabTTabTR988EG2fVq1aiWbzXbFr+X+/ftz3Q7yLvN7a//+/c62Pn36ZPkaFJa5c+eqYsWKSk1NLZL9uWvMmDFq1KiRMjIyzC4FhYwQg2vC4sWLNWbMmHw9Z/PmzRo/fjwhJo9OnDihXr166eabb9bKlSu1ZcsWhYaG5vocHx8fzZo1K0t7YmKi1q9fL19f3yzr3Pla4tp3/vx5jRw5UsOHD5ePj4/Z5eTq+eefV2JioubMmWN2KShkhBhcExo2bKibb77Z7DLy5eLFi7p06ZLZZeTZr7/+qosXL6pnz55q0aKF7rjjDnl7e+f6nG7dumnTpk3au3evS/vs2bNVpUoVNWvWLMtzrPi1dNeFCxd0o3z83Jw5c3Ty5EkNGDDA7FKuyM/PTz179tSUKVNumK/PjYoQg2vC5acgMjIyNHHiRIWFhcnLy0tlypRR/fr19eabb0qSxo0bp3/961+SpOrVqztPfaxfv975/KlTp6pWrVqy2+3y9/dX7969dejQIZf9GoahSZMmKSQkRJ6engoPD9fq1asVERGhiIgIZ7/M0ysffvihnnvuOVWpUkV2u1379u3TiRMnNHjwYNWpU0elS5eWv7+/WrVqpY0bN7rsK/O0yrRp0/Tqq6+qWrVq8vLyUkREhDNgvPjii6pcubL8/PzUtWtXHT9+PE/j9+WXX6pp06by9vaWj4+P2rRpoy1btjjX9+nTR82bN5f0dzCx2Wwury8nbdq0UVBQkGbPnu3ytZkzZ44iIyNVrFjWHyF5PTW4d+9ede/eXf7+/rLb7apdu7beeecdlz5Xmgc5yfx6ffTRR4qKilJAQIC8vLzUokULff/991n6b9++Xffdd5/KlSsnT09PNWzYUJ9++qlLn8xTOatWrVK/fv1UsWJFeXt7y+Fw5FjHTz/9pLZt28rb21sVK1bUkCFDtGzZMpe5KkmrV69Wly5dVLVqVXl6eqpGjRp68sknlZycfMVxzE5aWppGjBih6tWry8PDQ1WqVNGQIUOyHLWsVq2aOnXqpJUrV6pRo0by8vJSrVq1XL7emaKjo9W5c2eVKVPGpd1ms2no0KGKiYlxfp3Cw8MVFxcnwzA0bdo0Va9eXaVLl1arVq20b98+l+dHRESobt262rhxo+644w55eXmpSpUqGjNmjNLT0136Hjp0SA899JB8fHxUpkwZ9ejRQ9u2bcv2dGWvXr3066+/at26dW6NIayBEINCk56erkuXLmV55OUvo6lTp2rcuHF67LHHtGzZMn3yySfq37+/84fwgAED9NRTT0mSFi1apC1btmjLli1q1KiRJGnQoEEaPny42rRpoy+//FITJkzQypUrdeedd7r8Yhg1apRGjRqle++9V0uWLNHAgQM1YMAA/frrr9nWNWLECCUlJWnGjBlaunSp/P39derUKUnS2LFjtWzZMsXExOimm25SRESEyy+qTO+8846+/fZbvfPOO3r//ff1yy+/qHPnzurfv79OnDih2bNna+rUqfrmm2/y9FfvvHnz1KVLF/n6+mr+/PmaNWuW/vzzT0VERGjTpk2S/r5GIDMgTJo0SVu2bNF///vfK267WLFi6tOnj+bOnev8hbJq1SodOnRIffv2veLzc/Lzzz+rcePG+vHHH/Xaa6/pq6++UseOHfX0009r/Pjxzn5XmgdXMnLkSP3+++96//339f777+vIkSOKiIjQ77//7uyzbt06NWvWTKdPn9aMGTO0ZMkSNWjQQN26dcv2Op5+/fqpZMmS+vDDD/XZZ5+pZMmS2e776NGjatGihRISEhQdHa25c+cqNTVVQ4cOzdL3t99+U9OmTRUdHa1Vq1bppZde0nfffafmzZvr4sWLeXqtmQzD0P33369///vf6tWrl5YtW6aoqCjNmTNHrVq1yhK6du/ereeee07PPvuslixZovr166t///7asGGDs8+hQ4f0ww8/qGXLltnu86uvvtL777+vKVOmaP78+UpNTVXHjh313HPP6dtvv9Xbb7+td999Vz///LMefPDBLD8Djh07pkcffVQ9evTQkiVL9NBDD2nixIkaNmyYs8+5c+fUsmVLrVu3Tq+++qo+/fRTVapUSd26dcu2pttuu02lS5fWsmXL8jV+sBgDKGAxMTGGpFwfISEhLs8JCQkxIiMjncudOnUyGjRokOt+pk2bZkgyEhMTXdrj4+MNScbgwYNd2r/77jtDkjFy5EjDMAzj1KlTht1uN7p16+bSb8uWLYYko0WLFs62devWGZKMu++++4qv/9KlS8bFixeN1q1bG127dnW2JyYmGpKMW2+91UhPT3e2v/HGG4Yk47777nPZzjPPPGNIMs6cOZPjvtLT043KlSsb9erVc9lmamqq4e/vb9x5551ZXsPChQuv+Br+2ff33383bDab8dVXXxmGYRgPP/ywERERYRiGYXTs2PGKX8vM1x0TE+Nsa9eunVG1atUsr23o0KGGp6encerUKcMw8jYPcqu/UaNGRkZGhrN9//79RsmSJY0BAwY422rVqmU0bNjQuHjxoss2OnXqZAQGBjrHNXNe9+7dO081/Otf/zJsNpvx008/ubS3a9fOkGSsW7cu2+dlZGQYFy9eNA4cOGBIMpYsWeJcl1nDP+d8ZGSky9dg5cqVhiRj6tSpLtv95JNPDEnGu+++62wLCQkxPD09jQMHDjjbLly4YJQrV8548sknszw3Li4uS72SjICAAOPs2bPOti+++MKQZDRo0MBl/DPn+p49e5xtLVq0yPI6DcMwHn/8caNYsWLO2t555x1DkrFixQqXfk8++WSW+ZWpWbNmRpMmTbK04/rBkRgUmrlz52rbtm1ZHpmnNXJz++23a/fu3Ro8eLC+/vprpaSk5Hm/mYePLz+lcfvtt6t27dpas2aNJCkuLk4Oh0OPPPKIS7877rgjx3d7PPjgg9m2z5gxQ40aNZKnp6dKlCihkiVLas2aNYqPj8/St0OHDi6nYWrXri1J6tixo0u/zPakpKQcXqmUkJCgI0eOqFevXi7bLF26tB588EHFxcXp/PnzOT4/L6pXr66IiAjNnj1bJ0+e1JIlS9SvXz+3t5eWlqY1a9aoa9eu8vb2djlK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vys6OlpRUVEaOXKktm7dqqefflp2u129e/fO0t/hcMjhcDiXU1JSirJcFJKkpCQlJyebXUa+OBwO2e12s8vIlwoVKig4ONjsMgCgwNgMwzDM2rmHh4fCw8O1efNmZ9vTTz+tbdu2acuWLVn6jxs3TuPHj8/SfubMGfn6+hZqrSgcSUlJCgurrbS082aXkk/FJaWbXUS+eHp6KyEhniADwHQpKSny8/O76t/fph6JCQwMVJ06dVzaateurc8//zzb/iNGjFBUVJRzOSUlRUFBQYVaIwpXcnLy/wLMR5Jqm11OHi2XNEbWqjleaWk9lZycTIgBcN0wNcQ0a9ZMCQkJLm2//vqrQkJCsu1vt9stdwgfeVVbUiOzi8ij+P/9a6WaAeD6Y+qFvc8++6zi4uI0adIk7du3T/PmzdO7776rIUOGmFkWAACwAFNDTOPGjbV48WLNnz9fdevW1YQJE/TGG2+oR48eZpYFAAAswNTTSZLUqVMnderUyewyAACAxZj+sQMAAADuIMQAAABLIsQAAABLIsQAAABLIsQAAABLIsQAAABLIsQAAABLIsQAAABLIsQAAABLIsQAAABLIsQAAABLIsQAAABLIsQAAABLIsQAAABLIsQAAABLIsQAAABLIsQAAABLIsQAAABLIsQAAABLIsQAAABLIsQAAABLIsQAAABLIsQAAABLIsQAAABLIsQAAABLIsQAAABLIsQAAABLIsQAAABLIsQAAABLIsQAAABLIsQAAABLIsQAAABLIsQAAABLIsQAAABLIsQAAABLIsQAAABLIsQAAABLIsQAAABLIsQAAABLIsQAAABLIsQAAABLIsQAAABLIsQAAABLIsQAAABLIsQAAABLIsQAAABLIsQAAABLIsQAAABLMjXEjBs3TjabzeUREBBgZkkAAMAiSphdwC233KJvvvnGuVy8eHETqwEAAFZheogpUaIER18AAEC+mR5i9u7dq8qVK8tut6tJkyaaNGmSbrrppmz7OhwOORwO53JKSkpRlQlcF+Lj480uIV8qVKig4OBgs8sAcI0yNcQ0adJEc+fOVWhoqP744w9NnDhRd955p3766SeVL18+S//Jkydr/PjxJlQKWN1RScXUs2dPswvJF09PbyUkxBNkAGTL1BDTvn175//r1aunpk2b6uabb9acOXMUFRWVpf+IESNc2lNSUhQUFFQktQLWdlpShqSPJNU2t5Q8i1daWk8lJycTYgBky/TTSf9UqlQp1atXT3v37s12vd1ul91uL+KqgOtJbUmNzC4CAArENXWfGIfDofj4eAUGBppdCgAAuMaZGmKef/55xcbGKjExUd99950eeughpaSkKDIy0syyAACABZh6OunQoUN67LHHlJycrIoVK+qOO+5QXFycQkJCzCwLAABYgKkhZsGCBWbuHgAAWNg1dU0MAABAXhFiAACAJRFiAACAJRFiAACAJRFiAACAJRFiAACAJRFiAACAJRFiAACAJRFiAACAJRFiAACAJRFiAACAJRFiAACAJRFiAACAJRFiAACAJRFiAACAJRFiAACAJRFiAACAJRFiAACAJRFiAACAJRFiAACAJRFiAACAJRFiAACAJRFiAACAJRFiAACAJRFiAACAJRFiAACAJRFiAACAJRFiAACAJRFiAACAJRFiAACAJRFiAACAJRFiAACAJRFiAACAJRFiAACAJRFiAACAJRFiAACAJRFiAACAJRFiAACAJRFiAACAJRFiAACAJRFiAACAJRFiAACAJRFiAACAJRFiAACAJRFiAACAJRFiAACAJRFiAACAJRFiAACAJV0zIWby5Mmy2Wx65plnzC4FAABYwDURYrZt26Z3331X9evXN7sUAABgEaaHmLNnz6pHjx567733VLZsWbPLAQAAFlHC7AKGDBmijh076p577tHEiRNz7etwOORwOJzLKSkphV2e5SQlJSk5OdnsMvIsPj7e7BIAABZlaohZsGCBdu7cqW3btuWp/+TJkzV+/PhCrsq6kpKSFBZWW2lp580uBQCAQmdaiDl48KCGDRumVatWydPTM0/PGTFihKKiopzLKSkpCgoKKqwSLSc5Ofl/AeYjSbXNLiePlksaY3YRAAALMi3E7NixQ8ePH9dtt93mbEtPT9eGDRv09ttvy+FwqHjx4i7PsdvtstvtRV2qBdWW1MjsIvKI00kAAPeYFmJat26tH374waWtb9++qlWrloYPH54lwAAAAPyTaSHGx8dHdevWdWkrVaqUypcvn6UdAADgcqa/xRoAAMAdpr/F+p/Wr19vdgkAAMAiOBIDAAAsiRADAAAsiRADAAAsiRADAAAsiRADAAAsiRADAAAsiRADAAAsiRADAAAsiRADAAAsiRADAAAsya0Qk5iYWNB1AAAA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06bpt99+k2EYqlGjhkqVKlXQ9QEAAGTrqj4A8ujRozp69KhCQ0NVqlQpGYZRUHUBAADkyq0Qc/LkSbVu3VqhoaHq0KGDjh49KkkaMGBAnt+ZBAAAcDXcCjHPPvusSpYsqaSkJHl7ezvbu3Xrxj1eAABAkXDrmphVq1bp66+/VtWqVV3aa9asqQMHDhRIYQAAALlx60jMuXPnXI7AZEpOTuZjAQAAQJFwK8Tcfffdmjt3rnPZZrMpIyND06ZNU8uWLQusOAAAgJy4dTpp2rRpioiI0Pbt2/XXX3/phRde0E8//aRTp07p22+/LegaAQAAsnDrSEydOnW0Z88e3X777WrTpo3OnTunBx54QN9//71uvvnmgq4RAAAgi3wfibl48aLatm2rmTNnavz48YVREwAAwBXl+0hMyZIl9eOPP8pmsxVGPQAAAHni1umk3r178wnUAADAVG5d2PvXX3/p/fff1+rVqxUeHp7lM5OmT59eIMUBAADkJF8h5vfff1e1atX0448/qlGjRpKkX3/91aUPp5kAAEBRyFeIqVmzpo4ePap169ZJ+vtjBt566y1VqlSpUIoDAADISb6uibn8U6pXrFihc+fOFWhBAAAAeeHWhb2ZLg81AAAARSVfIcZms2W55oVrYAAAgBnydU2MYRjq06eP80Me09LSNHDgwCzvTlq0aFHBVQgAAJCNfIWYyMhIl+WePXsWaDEAAAB5la8QExMTU1h1AAAA5MtVXdgLAABgFkIMAACwJEIMAACwJEIMAACwJEIMAACwJEIMAACwJEIMAACwJEIMAACwJEIMAACwJEIMAACwJEIMAACwJEIMAACwJEIMAACwJEIMAACwJEIMAACwJEIMAACwJEIMAACwJEIMAACwJEIMAACwJEIMAACwJEIMAACwJEIMAACwJEIMAACwJEIMAACwJEIMAACwJFNDzOTJk9W4cWP5+PjI399f999/vxISEswsCQAAWISpISY2NlZDhgxRXFycVq9erUuXLqlt27Y6d+6cmWUBAAALKGHmzleuXOmyHBMTI39/f+3YsUN33323SVUBAAArMDXEXO7MmTOSpHLlymW73uFwyOFwOJdTUlIKtZ6kpCQlJycX6j4KUnx8vNklAECRsNrP50wOh0N2u93sMvKlQoUKCg4ONruMbF0zIcYwDEVFRal58+aqW7dutn0mT56s8ePHF0k9SUlJCgurrbS080WyPwBA3lj753NxSelmF5Evnp7eSkiIvyaDzDUTYoYOHao9e/Zo06ZNOfYZMWKEoqKinMspKSkKCgoqlHqSk5P/9w3ykaTahbKPgrdc0hiziwCAQmXNn8/S//+MtlLd8UpL66nk5GRCTE6eeuopffnll9qwYYOqVq2aYz+73W7CYbjakhoV8T7dxekkADcSK/18lv7/Z7TV6r52mRpiDMPQU089pcWLF2v9+vWqXr26meUAAAALMTXEDBkyRPPmzdOSJUvk4+OjY8eOSZL8/Pzk5eVlZmkAAOAaZ+p9YqKjo3XmzBlFREQoMDDQ+fjkk0/MLAsAAFiA6aeTAAAA3MFnJwEAAEsixAAAAEsixAAAAEsixAAAAEsixAAAAEsixAAAAEsixAAAAEsixAAAAEsixAAAAEsixAAAAEsixAAAAEsixAAAAEsixAAAAEsixAAAAEsixAAAAEsixAAAAEsixAAAAEsixAAAAEsixAAAAEsixAAAAEsixAAAAEsixAAAAEsixAAAAEsixAAAAEsixAAAAEsixAAAAEsixAAAAEsixAAAAEsixAAAAEsixAAAAEsixAAAAEsixAAAAEsixAAAAEsixAAAAEsixAAAAEsixAAAAEsixAAAAEsixAAAAEsixAAAAEsixAAAAEsixAAAAEsixAAAAEsixAAAAEsixAAAAEsixAAAAEsixAAAAEsixAAAAEsixAAAAEsyNcRs2LBBnTt3VuXKlWWz2fTFF1+YWQ4AALAQU0PMuXPndOutt+rtt982swwAAGBBJczcefv27dW+fXszSwAAABZlaojJL4fDIYfD4VxOSUkxsRoAyF58fLzZJeSLw+GQ3W43u4w8s9r4ovBYKsRMnjxZ48ePN7sMAMjBUUnF1LNnT7MLyafiktLNLgLIN0uFmBEjRigqKsq5nJKSoqCgIBMrAoB/Oi0pQ9JHkmqbW0qeLZc0RtasGTc6S4UYu91uqUOeAG5UtSU1MruIPMo8NWPFmnGj4z4xAADAkkw9EnP27Fnt27fPuZyYmKhdu3apXLlyCg4ONrEyAABwrTM1xGzfvl0tW7Z0Lmde7xIZGakPPvjApKoAAIAVmBpiIiIiZBiGmSUAAACL4poYAABgSYQYAABgSYQYAABgSYQYAABgSYQYAABgSYQYAABgSYQYAABgSYQYAABgSYQYAABgSYQYAABgSYQYAABgSYQYAABgSYQYAABgSYQYAABgSYQYAABgSYQYAABgSYQYAABgSYQYAABgSYQYAABgSYQYAABgSYQYAABgSYQYAABgSYQYAABgSYQYAABgSYQYAABgSYQYAABgSYQYAABgSYQYAABgSYQYAABgSYQYAABgSYQYAABgSYQYAABgSYQYAABgSYQYAABgSYQYAABgSYQYAABgSYQYAABgSYQYAABgSYQYAABgSYQYAABgSYQYAABgSYQYAABgSYQYAABgSYQYAABgSYQYAABgSYQYAABgSYQYAABgSaaHmP/+97+qXr26PD09ddttt2njxo1mlwQAACzA1BDzySef6JlnntGoUaP0/fff66677lL79u2VlJRkZlkAAMACTA0x06dPV//+/TVgwADVrl1bb7zxhoKCghQdHW1mWQAAwAJMCzF//fWXduzYobZt27q0t23bVps3bzapKgAAYBUlzNpxcnKy0tPTValSJZf2SpUq6dixY9k+x+FwyOFwOJfPnDkjSUpJSSnw+s6ePfu//+2QdDa3rteQ+P/9S82Fi5qLBjUXDWouOlasO0HS378TC/J3bea2DMO4ug0ZJjl8+LAhydi8ebNL+8SJE42wsLBsnzN27FhDEg8ePHjw4MHjOngcPHjwqrKEaUdiKlSooOLFi2c56nL8+PEsR2cyjRgxQlFRUc7ljIwMnTp1SuXLl5fNZsvX/lNSUhQUFKSDBw/K19c3/y8AV4XxNxfjby7G31yMv7kyx//nn39W5cqVr2pbpoUYDw8P3XbbbVq9erW6du3qbF+9erW6dOmS7XPsdrvsdrtLW5kyZa6qDl9fXyaxiRh/czH+5mL8zcX4m6tKlSoqVuzqLs01LcRIUlRUlHr16qXw8HA1bdpU7777rpKSkjRw4EAzywIAABZgaojp1q2bTp48qZdffllHjx5V3bp1tXz5coWEhJhZFgAAsABTQ4wkDR48WIMHDy7y/drtdo0dOzbL6SkUDcbfXIy/uRh/czH+5irI8bcZxtW+vwkAAKDomf7ZSQAAAO4gxAAAAEsixAAAAEsixAAAAEu67kPMhg0b1LlzZ1WuXFk2m01ffPGFy3rDMDRu3DhVrlxZXl5eioiI0E8//WROsdehK41/nz59ZLPZXB533HGHOcVeZyZPnqzGjRvLx8dH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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.hist(mtcars['mpg'],bins=10,color='blue',edgecolor='black')\n",
    "plt.xlabel('Miles per gallon(mpg)')\n",
    "plt.ylabel('Frequency')\n",
    "plt.title('Histogram of Miles per gallon(mpg)')\n",
    "plt.show()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
