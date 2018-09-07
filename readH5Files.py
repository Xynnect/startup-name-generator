# import h5py
# filename = 'models/gallicc_500epochs.h5'
# f = h5py.File(filename, 'r')
#
# print(f)

# # List all groups
# print("Keys: %s" % f.keys())
# a_group_key = list(f.keys())[0]
#
# # Get the data
# data = list(f[a_group_key])
# print(data)


# import h5py
#
# filename = 'models/gallicc_500epochs.h5'
# data = h5py.File(filename, 'r')
#
# print(list(data))


import h5py
filename = 'models/gallicc_500epochs.h5'
f = h5py.File(filename, 'r')

print(list(f))

# print(f['model_weights'])
#
# print(dir(f['model_weights']))
#
# print(type(f['model_weights']))

tmp = f['optimizer_weights']
for x in tmp:
    x.encode('utf-8')
    print(x)

# print(f['model_weights'].encode('utf-8'))

# print(f['model_weights'][30])


# # List all groups
# print("Keys: %s" % f.keys())
# a_group_key = list(f.keys())[0]
#
# # Get the data
# data = list(f[a_group_key])
# print(data)




# In [1]: import h5py
#
# In [2]: f = h5py.File("kappa-m111111.hdf5")
#
# In [3]: list(f)
# Out[3]:
# ['frequency',
#  'gamma',
#  'group_velocity',
#  'gv_by_gv',
#  'heat_capacity',
#  'kappa',
#  'kappa_unit_conversion',
#  'mesh',
#  'mode_kappa',
#  'qpoint',
#  'temperature',
#  'weight']
#
# In [4]: f['kappa'].shape
# Out[4]: (101, 6)
#
# In [5]: f['kappa'][:]

# for key in data.keys():
#     print(key) #Names of the groups in HDF5 file.
# #Get the HDF5 group
#     group = data[key]
#     print(group)
#
#     list(group)
#     # data = group[key]
#
# #Checkout what keys are inside that group.
# # for key in group.keys():
# #     print(key)
#
    # data = group[key].value
#Do whatever you want with data
