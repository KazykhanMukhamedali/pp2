# Some Values are False

# ex1
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# ex2
class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))