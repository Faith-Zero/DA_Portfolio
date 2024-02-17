select * from PortfolioProject..Covid_Deaths
order by 3,2,4

select * from PortfolioProject..Covid_Vacinations
order by 3,2,4

Select Location, date, Total_cases, New_cases, Total_Deaths, Population 
from PortfolioProject..Covid_Deaths order by 1,2

--ALTER TABLE PortfolioProject..Covid_Deaths ALTER COLUMN Total_cases int;
--ALTER TABLE PortfolioProject..Covid_Deaths ALTER COLUMN Total_deaths int;

--Total Cases vs Total Deaths --CAST is used to transform the integer data type into a decimal number so it can represent the percentage more accurately

Select Location, Date, Total_cases, Total_deaths, (Cast(Total_deaths as decimal(18,2))/(Cast(Total_cases as decimal(18,2)))*100) Death_Percentage
from PortfolioProject..Covid_Deaths 
where location like '%state%'
AND total_cases is not null
AND total_deaths is not null
order by 1,2

-- Total Cases vs Population
-- Shows whhat percentage of population got Covid

Select Location, Date, Population, Total_cases, (Cast(Total_cases as decimal(18,2))/(Cast(Population as decimal(18,2)))*100) Infected_Percentage
from PortfolioProject..Covid_Deaths 
where total_cases is not null
order by 5 desc, 2, 1

-- Countries with Highest infection Rate compared to Population

Select Location, Population, Max(Total_cases) Infection_Count, Max((Cast(Total_cases as decimal(18,2))/(Cast(Population as decimal(18,2)))*100)) Infection_Rate
from PortfolioProject..Covid_Deaths 
where continent is not null
and location like '%philip%'
group by location, population
order by 4 desc,3,1

-- Countries with Highest Death Count per Population

/* Select Location, Population, Max(Total_deaths) Death_Count, Max((Cast(total_deaths as decimal(18,2))/(Cast(Population as decimal(18,2)))*100)) Death_Rate
from PortfolioProject..Covid_Deaths 
where continent is not null
and location like '%philip%'
group by location, population
order by 4 desc,2 desc, 3, 1 */

Select location, Max(cast(Total_deaths as int)) as Total_Death_Count
from PortfolioProject..Covid_Deaths
where continent is null
group by location
order by Total_Death_Count desc

-- Global Numbers
Select date, sum(cast(new_cases as int)) New_Cases, sum(cast(new_deaths as int)) New_Deaths, case when cast(new_cases as int) = 0 then 1 else (sum(cast(new_deaths as decimal(18,2))) / sum(cast(new_cases as decimal(18,2)))) *100 end as Death_Rate
from PortfolioProject..Covid_Deaths
where continent is not null
group by date, new_cases, new_deaths
order by 4 desc, 1-- percentage of death rate upon infection

--CTE - Common Table Expressions
With People_Vaccinated2 (Continent, Location, Date, Population, New_Vaccinations, Cummulative_Vaccinations)
as(
Select cd.continent, cd.location, cd.date, cd.population, min(cv.new_vaccinations), sum(cv.new_vaccinations) over (partition by cd.location order by cd.location, cd.date) as Cummulative_Vaccinations
from PortfolioProject..Covid_Deaths cd
join PortfolioProject..Covid_Vacinations cv
on cd.date = cv.date 
and cd.location = cv.location
and cd.iso_code = cv.iso_code
where cv.new_vaccinations is not null
and cd.continent is not null
group by cd.location, cd.date, cd.continent, cd.population, cv.new_vaccinations
)
Select * from People_Vaccinated2

-- Temp Table
Drop Table if exists People_Vaccinated
Create Table dbo.People_Vaccinated (
Continent nvarchar(255),
Location nvarchar(255),
Date datetime,
Population Int,
New_Vaccinations int,
Cummulative_Vaccinations numeric
)
Insert into People_Vaccinated
Select cd.continent, 
	   cd.location, 
	   cd.date, 
	   cd.population, 
	   min(cv.new_vaccinations), 
	   sum(cv.new_vaccinations) over (partition by cd.location order by cd.location, cd.date) as Cummulative_Vaccinations
from PortfolioProject..Covid_Deaths cd
join PortfolioProject..Covid_Vacinations cv
on cd.date = cv.date 
and cd.location = cv.location
and cd.iso_code = cv.iso_code
where cv.new_vaccinations is not null
and cd.continent is not null
group by cd.location, cd.date, cd.continent, cd.population, cv.new_vaccinations
order by 2, 3

Select Continent, Location, Date, Population, New_vaccinations, Cummulative_Vaccinations,
(cast(New_vaccinations as decimal(18,2))/cast(Population as decimal(18,2))*100) Vaccination_Rate,
(Cummulative_Vaccinations/Population)*100 Total_Vaccination_Rate
from People_Vaccinated


-- View
Create View dbo.People_Vaccinated2 as
Select cd.continent, cd.location, cd.date, cd.population, min(cv.new_vaccinations) New_Vaccinations, sum(cv.new_vaccinations) over (partition by cd.location order by cd.location, cd.date) as Cummulative_Vaccinations
from PortfolioProject..Covid_Deaths cd
join PortfolioProject..Covid_Vacinations cv
on cd.date = cv.date 
and cd.location = cv.location
and cd.iso_code = cv.iso_code
where cv.new_vaccinations is not null
and cd.continent is not null
group by cd.location, cd.date, cd.continent, cd.population, cv.new_vaccinations
