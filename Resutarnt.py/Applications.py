class Applications:
    def __init__(self):
        self.jobs = {
            "waiter": False,
            "chef": False,
            "cooker": False,
            "manager": False
        }

    def Apply(self, job, levels):
        job = job.lower()

        if job not in self.jobs:
            print("That job does not exist.")
            return False

        if self.jobs[job]:
            print(f"You have already applied for the {job} job.")
            return False

        print(f"\n--- {job.upper()} APPLICATION ---")

        experience = input(
            "Do you have experience? (yes/no): "
        ).strip().lower()

        effort = input(
            "Will you work hard? (yes/no): "
        ).strip().lower()

        customer = input(
            "Are you good with customers? (yes/no): "
        ).strip().lower()

        score = 0

        if experience == "yes":
            score += 1

        if effort == "yes":
            score += 1

        if customer == "yes":
            score += 1

        if job == "manager":
            decision = input(
                "Would you take responsibility for the restaurant? (yes/no): "
            ).strip().lower()

            if decision == "yes":
                score += 1

        if job == "chef":
            cooking = input(
                "Can you cook? (yes/no): "
            ).strip().lower()

            if cooking == "yes":
                score += 1

        if job == "cooker":
            speed = input(
                "Can you work quickly? (yes/no): "
            ).strip().lower()

            if speed == "yes":
                score += 1

        if job == "waiter":
            service = input(
                "Can you provide good customer service? (yes/no): "
            ).strip().lower()

            if service == "yes":
                score += 1

        self.jobs[job] = True

        if score >= 4:
            print(f"\nYou have been hired as a {job}!")
            levels.Achievement(f"Hired as {job.title()}", 25)
            return True

        if score == 3:
            print(f"\nYou passed the application for {job}.")
            print("You have been given a trial shift.")

            trial = input(
                "Do you want to accept the trial shift? (yes/no): "
            ).strip().lower()

            if trial == "yes":
                print(f"You are now working as a trial {job}.")
                levels.Achievement(f"Trial {job.title()}", 15)
                return True

            print("You rejected the trial shift.")
            return False

        print(f"\nYour application for {job} was rejected.")
        return False

    def ShowApplications(self):
        print("\n--- APPLICATIONS ---")

        for job, applied in self.jobs.items():
            if applied:
                print(f"{job.title()}: Applied")
            else:
                print(f"{job.title()}: Not Applied")

            if NameError:
                print("name is not recongised please try again later, because of the interruption of your service," \
                "I recommmended that you will get not applied for the inconvention of the job.")
            