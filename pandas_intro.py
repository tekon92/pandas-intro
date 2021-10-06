import pandas as pd

'''Masukan Data ke Dataframe'''
camp = pd.read_csv('/content/marketing_campaign.csv', sep='\t')

# Cek apakah ada kolom yang memiliki empty value
camp.isnull()

# Cek mana kolom yang categorical dan numerical
from pandas.core.dtypes.common import is_any_int_dtype
 
is_any_int_dtype(camp['ID'])

from pandas.core.dtypes.common import is_string_dtype
is_string_dtype(camp['Marital_Status'])


# Cek unique values dari kolom 'education' dan 'martial_status'
camp[['Education','Marital_Status']].value_counts()
# or
camp['Education'].value_counts()
camp['Marital_Status'].value_counts()


# Cek minimum dan maximum dari tahun lahir customer
camp['Year_Birth'].agg(['min','max'])


# Ubah nama kolom agar semuanya lowercase
camp.columns = map(str.lower, camp.columns)
camp.head()


# Isi data kosong di kolom 'income' menggunakan rata-rata 'income'
camp['income'].mean()
camp[camp['income'].isnull() == True] = camp['income'].mean()
camp


# Buat kolom baru 'age', untuk memasukkan usia customer berdasarkan tahun lahir
# import datetime
from datetime import datetime
from datetime import date
# pd.to_datetime('now').year
# pd.to_datetime('now').year - camp['year_birth']
 
camp['age'] = pd.to_datetime('now').year - camp['year_birth']
# camp['age']


# Buat kolom baru 'age_group' untuk mengkategorikan usia dari customer, dengan syarat: usia dibawah 21
# tahun adalah 'teenager', usia dibawah 50 tahun 'worker', usia diatas itu 'boomer'
# camp[camp['age'] < 21]
 
def get_status(df):
 if df['age'] < 21:
   return 'Teenager'
 elif df['age'] < 50:
   return 'Worker'
 else:
   return 'Boomer'
 
camp['age_group'] = camp.apply(get_status, axis = 1)
camp[camp['age'] > 21][['age', 'age_group']]

# Urutkan data customer berdasarkan pembelian hari pembelian terbaru dan penghasilan tertinggi
# camp.reset_index()
# camp['dt_customer'] = pd.to_datetime(camp['dt_customer'])
 
camp.sort_values(by=['dt_customer', 'income'], ascending=[False, True])


# Simpan data ke bentuk excel dengan nama file 'customer_enhanced'
camp.to_excel('customer_enhanced.xlsx', sheet_name='clean', index=False)
