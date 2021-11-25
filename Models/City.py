import random
from traits.api import HasTraits

class City( HasTraits ):
    name = ""
    populationRanges = {
        "homestead": [1, 49],
        "tiny": [50, 299],
        "small": [300, 4999],
        "medium": [5000, 14999],
        "large": [15000, 99999],
        "huge": [100000, 1000000000]
    }
    population = 0

    safetyLevel = ""
    threatLevel = ""
    safetyLevelNames = {
        "very unsafe": [1, 19],
        "unsafe": [20, 39],
        "neutral": [40, 59],
        "safe": [60, 79],
        "very safe": [80, 100]
    }
    threatLevelNames = {
        "low": [1, 19],
        "moderate": [20, 39],
        "substantial": [40, 59],
        "severe": [60, 79],
        "critical": [80, 100]
    }

    imports = {}
    exports = {}
    importCashFlow = 0
    exportCashFlow = 0

    # story lines to add some flair to the changes within the city walls
    increaseThreatLines = [
        "Raiding parties hit the walls"
    ]
    decreaseThreatLines = [
        "City Guard hires rangers to patrol the nearby forests"
    ]
    increaseSafetyLines = [
        "Local Security forces recruit more soldiers"
    ]
    decreaseSafetyLines = [
        "Gangs overtake a district"
    ]
    increasePopulationLines = [
        "Settlers arrive in town"
    ]
    decreasePopulationLines = [
        "Disease infects local water source"
    ]

    def __init__(self, name, size):
        # Name the city
        self.name = name

        # Randomly determine start population
        if size in self.populationRanges:
            self.population = random.randint(self.populationRanges[size][0],self.populationRanges[size][1])
        else:
            self.population = 1

        # Randomly determine threat and safety levels
        # this will be determined by or impact the following
        # 1) How well protected the city is (city guard)
        # 2) How corrupt the guards are
        # 3) How well the city is policed within
        # 4) How corrupt the internal police are
        # 5) What external threats exist? Raiders, barbarians, rival cities, tribes, contested borders, disputed trade routes
        # 6) What internal threats exist? Ruffians, gangs, disease
        self.safetyLevel = random.randint(1,100)
        self.threatLevel = random.randint(1,100)

    def getName(self):
        return self.name

    def getPopulation(self):
        return self.population

    def getSize(self):
        for size in self.populationRanges:
            if self.populationRanges[size][0] <= self.population <= self.populationRanges[size][1]:
                return size

    def getSafety(self):
        for safety in self.safetyLevelNames:
            if self.safetyLevel >= self.safetyLevelNames[safety][0] and self.safetyLevel <= self.safetyLevelNames[safety][1]:
                return safety

    def getThreat(self):
        for threat in self.threatLevelNames:
            if self.threatLevel >= self.threatLevelNames[threat][0] and self.threatLevel <= self.threatLevelNames[threat][1]:
                return threat

    # Skip ahead number of days
    # every week re-assess safety and threat levels
    # every day re-assess population
    # every month re-assess finances
    def passDays(self, days):
        story = []
        for day in range(days):
            # City is a ghost town
            if day%7 == 0:
                population = self.population
                # assess population
                self.updatePopulation()
                if self.population == 0:
                    print("Entire population has either died or moved away")
                    return

            safetyLevel = self.safetyLevel
            threatLevel = self.threatLevel
            if day%30 == 0:
                #re-assess safety and threat levels
                self.updateSafety()
                self.updateThreat()

            if day%90 == 0:
                #re-assess finances
                self.updateImports()
                self.updateExports()

            if safetyLevel > self.safetyLevel:
                story.append(random.choice(self.increaseSafetyLines))
            elif safetyLevel < self.safetyLevel:
                story.append(random.choice(self.decreaseSafetyLines))

            if threatLevel > self.threatLevel:
                story.append(random.choice(self.increaseThreatLines))
            elif threatLevel < self.threatLevel:
                story.append(random.choice(self.decreaseThreatLines))

        for line in story:
            print(line)

    def updatePopulation(self):
        currentSize = ''
        for size in self.populationRanges:
            if self.populationRanges[size][0] <= self.population <= self.populationRanges[size][1]:
                currentSize = size

        previousSize = 'homestead'
        for size in self.populationRanges:
            if size == currentSize:
                break;
            else:
                previousSize = size

        if previousSize == currentSize:
            if self.population > 1:
                populationChange = random.randint(self.populationRanges[previousSize][0], self.population - 1)
            else:
                populationChange = random.randint(0, 1)
        else:
            populationChange = random.randint(self.populationRanges[previousSize][0], self.populationRanges[previousSize][1])

        # skewed based on the threat/safety levels
        threshold = 50
        threshold += random.randint(self.safetyLevelNames[self.getSafety()][0], self.safetyLevelNames[self.getSafety()][1])
        threshold -= random.randint(self.threatLevelNames[self.getThreat()][0], self.threatLevelNames[self.getThreat()][1])

        if random.randint(0,100) >= threshold:
            self.population -= populationChange
        else:
            self.population += populationChange

    def updateSafety(self):
        currentSafety = self.getSafety()
        previousSafety = "very unsafe"
        for safety in self.safetyLevelNames:
            if self.safetyLevelNames[safety][0] <= self.safetyLevel <= self.safetyLevelNames[safety][1]:
                break;
            else:
                previousSafety = safety

        safetyChange = random.randint(self.safetyLevelNames[previousSafety][0], self.safetyLevelNames[previousSafety][1])

        if random.randint(0,1) == 0:
            self.safetyLevel -= safetyChange
        else:
            self.safetyLevel += safetyChange

        if self.safetyLevel > 100:
            self.safetyLevel = 100;
        if self.safetyLevel <= 0:
            self.safetyLevel = 1;

    def updateThreat(self):
        currentThreat = self.getThreat()
        previousThreat = "low"
        for threat in self.threatLevelNames:
            if self.threatLevelNames[threat][0] <= self.threatLevel <= self.threatLevelNames[threat][1]:
                break;
            else:
                previousThreat = threat

        threatChange = random.randint(self.threatLevelNames[previousThreat][0], self.threatLevelNames[previousThreat][1])

        if random.randint(0, 1) == 0:
            self.threatLevel -= threatChange
        else:
            self.threatLevel += threatChange

        if self.threatLevel > 100:
            self.threatLevel = 100
        if self.threatLevel <= 0:
            self.threatLevel = 1

    def updateImports(self):
        return ""

    def updateExports(self):
        return ""