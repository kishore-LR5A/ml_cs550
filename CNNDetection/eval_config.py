from util import mkdir


# directory to store the results
results_dir = './results/'
mkdir(results_dir)

# root to the testsets
dataroot = './dataset/test/'

# list of synthesis algorithms
vals = ['progan', 'biggan', 'cyclegan', 'stargan', 'gaugan',
        'crn', 'imle', 'seeingdark', 'san', 'deepfake']

# indicates if corresponding testset has multiple classes
multiclass = [1, 0, 1, 0, 0, 0, 0, 0, 0, 0]

# model
model_path = 'weights/blur_jpg_prob0.5.pth'

# list of synthesis algorithms
vals = ['progan', 'biggan', 'cyclegan', 'stargan', 'gaugan',
        'crn', 'imle', 'seeingdark', 'san', 'deepfake']

# indicates if corresponding testset has multiple classes
multiclass = [1, 0, 1, 0, 0, 0, 0, 0, 0, 0]
