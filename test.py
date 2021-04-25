
f=open("/.deepsource.toml","r")
f.write("config file.")
f.close()


def get_number(self,min_max=[1,10]):
  assert all([isinstance(i,int) for i in min_max])
  return random.randint(*min_max)
