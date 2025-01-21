class Model:
    def __init__(self):
        self.model = {}

    def __str__(self):
        if self.model:
            return f'Model: ' + ', '.join([f'{key}={value}' for key, value in self.model.items()])
        else:
            return "Model"

    def query(self, **kwargs):
        self.model = dict(kwargs)


########################################################################################################################

model = Model()
model.query(id=1, fio='Sergey', old=33)
print(model)

########################################################################################################################

# class Model:
#     def query(self, **kwargs):
#         self.dquery = kwargs
# 
#     def __str__(self):
#         try:
#             return "Model: " + ', '.join(f"{k} = {v}" for k, v in self.dquery.items())
#         except AttributeError:
#             return "Model"