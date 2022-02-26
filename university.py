class Admission:
    departments = {'Physics': [1, 3], 'Mathematics': [3], 'Biotech': [2, 1], 'Chemistry': [2], 'Engineering': [4, 3]}
    applicants = []
    accepted = {}

    def __init__(self, app_no):
        self.app_no = app_no

    def read_applicants(self):
        with open('applicants.txt', 'r') as file:
            for line in file.readlines():
                line = line.split()
                self.applicants.append([" ".join(line[:2]), *map(float, line[2:7]), *line[7:]])

    def get_accepted(self):
        for priority in range(3):
            for department in self.departments:
                applicants = [[applicant[0], max(sum(applicant[i] for i in self.departments[department]) / len(self.departments[department]), applicant[5])]
                              for applicant in self.applicants if applicant[-3 + priority] == department]
                applicants = sorted(applicants, key=lambda x: (-x[-1], x[0]))
                if department not in self.accepted:
                    self.accepted[department] = []
                for applicant in applicants:
                    if len(self.accepted[department]) < self.app_no:
                        self.accepted[department].append(applicant)
                        [self.applicants.remove(value) for value in self.applicants if value[0] == applicant[0]]
                self.accepted[department] = sorted(self.accepted[department], key=lambda x: (-x[-1], x[0]))

    def save_accepted(self):
        for department in sorted(self.accepted):
            with open(department.lower() + '.txt', 'w') as file:
                print(*['{} {}'.format(*accepted) for accepted in self.accepted[department]], sep='\n', file=file)


admission = Admission(int(input()))
admission.read_applicants()
admission.get_accepted()
admission.save_accepted()
