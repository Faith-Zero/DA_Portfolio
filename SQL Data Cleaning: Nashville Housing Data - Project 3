--Data Cleaning using SQL Queries

/*
Things to Fix
1. SaleDate format
2. PropertyAddress has null values
3. SoldAsVacant has two types of answer Y, N, Yes and No
4. Duplicate Values
*/

Select *
From PortfolioProject.dbo.Nashville_DataSet
 --------------------------------------------------------------------------------------------------------------------------
-- 1. Standardize Date Format, find the correct format 
Select CONVERT(Date,SaleDate)
From PortfolioProject..Nashville_DataSet

-- Update Table
Update PortfolioProject..Nashville_DataSet
SET SaleDate = CONVERT(Date,SaleDate)

--Update is not working as intended, alternatively create a new column with the proper format then delete the column with incorrect format
Select SaleDate from PortfolioProject..Nashville_DataSet

-- Add SaleDateConverted Column
ALTER TABLE PortfolioProject..Nashville_DataSet
Add SaleDateConverted Date;

-- Insert correct format to SaleDateConverted
Update PortfolioProject..Nashville_DataSet
SET SaleDateConverted = CONVERT(Date,SaleDate)

-- Check if update is successful
Select SaleDateConverted from PortfolioProject..Nashville_DataSet

 --------------------------------------------------------------------------------------------------------------------------

-- 2. Populate Property Address data

Select *
From PortfolioProject..Nashville_DataSet
where PropertyAddress is null
order by ParcelID

-- ParcelID is the same to all of the property address so you can use it to populate the missing property address as long as parcel id is not null. Do this using self join
Select table1.ParcelID, table1.PropertyAddress, isnull(table1.PropertyAddress, table2.PropertyAddress) from PortfolioProject..Nashville_DataSet table1 
join PortfolioProject..Nashville_DataSet table2 on table1.ParcelID = table2.parcelID -- and table1.[UniqueID ] != table2.[UniqueID ]
where table1.[UniqueID ] != table2.[UniqueID ]

-- Update the table
Update table1
Set PropertyAddress = isnull(table1.PropertyAddress, table2.PropertyAddress) from PortfolioProject..Nashville_DataSet table1 
join PortfolioProject..Nashville_DataSet table2 on table1.ParcelID = table2.parcelID
where table1.[UniqueID ] != table2.[UniqueID ]

-- Check for null values
Select PropertyAddress from PortfolioProject..Nashville_DataSet where PropertyAddress is null
--------------------------------------------------------------------------------------------------------------------------

-- Seperate Address and City from property address
-- There are multiple functions similar to find such as CHARINDEX, DOES NOT WORK WITH MICROSOFT SQL (INSTR, LOCATE)
Select Propertyaddress, LEFT(propertyaddress,CHARINDEX(',', propertyaddress)-1), SUBSTRING(propertyaddress,CHARINDEX(',', propertyaddress)+1,CHARINDEX(',', propertyaddress)+1) --SUBSTRING(PropertyAddress, CHARINDEX(',', PropertyAddress) + 1 , LEN(PropertyAddress))
from PortfolioProject..Nashville_DataSet

-- Insert Address Column, City Column
Alter Table PortfolioProject..Nashville_DataSet 
Add PropertyAddress_Split Nvarchar(255);

Alter Table PortfolioProject..Nashville_DataSet 
Add PropertyCity Nvarchar(255);

-- Populate both Columns
Update PortfolioProject..Nashville_DataSet
Set PropertyAddress_Split = LEFT(propertyaddress,CHARINDEX(',', propertyaddress)-1);

Update PortfolioProject..Nashville_DataSet
Set PropertyCity = SUBSTRING(propertyaddress,CHARINDEX(',', propertyaddress)+1,CHARINDEX(',', propertyaddress)+1);

-- Check
Select PropertyAddress_Split, PropertyCity from PortfolioProject..Nashville_DataSet 

-----------------------------------------------------------------------------------------------------------------------------

Select Owneraddress from PortfolioProject..Nashville_DataSet 

-- Splitting the OwnerAddress into street, city, state
/*
Parsename read it in reverse don't know if always but in this case it reads it as STATE, CITY, STREET 
So parsename will return null if the delimeter is not period(.) that is why we needed to replace the commas(,) into period first
*/
Select PARSENAME(REPLACE(OwnerAddress,',','.'), 3),
PARSENAME(REPLACE(OwnerAddress,',','.'), 2),
PARSENAME(REPLACE(OwnerAddress,',','.'), 1)
from PortfolioProject..Nashville_DataSet 

-- Insert OwnerStreet, OwnerCity, OwnerState
ALTER TABLE PortfolioProject..Nashville_DataSet 
Add OwnerStreet Nvarchar(255);

ALTER TABLE PortfolioProject..Nashville_DataSet 
Add OwnerCity Nvarchar(255);

ALTER TABLE PortfolioProject..Nashville_DataSet 
Add OwnerState Nvarchar(255);

-- Update
Update PortfolioProject..Nashville_DataSet 
Set OwnerStreet = PARSENAME(REPLACE(OwnerAddress,',','.'), 3)

Update PortfolioProject..Nashville_DataSet 
Set OwnerCity = PARSENAME(REPLACE(OwnerAddress,',','.'), 2)

Update PortfolioProject..Nashville_DataSet 
Set OwnerState = PARSENAME(REPLACE(OwnerAddress,',','.'), 1)

-- Check
Select OwnerStreet, OwnerCity, OwnerState from PortfolioProject..Nashville_DataSet 
--------------------------------------------------------------------------------------------------------------------------


-- 3. Change Yes and No to Y and N
-- Use case though some versions of sql allow if but IF and CASE uses the same logic so its better to just use CASE since it is the more universal one than IF
Select Case when SoldAsVacant = 'Yes' Then 'Y' when SoldAsVacant = 'No' then 'N' end from PortfolioProject..Nashville_DataSet

Update PortfolioProject..Nashville_DataSet
Set SoldAsVacant = Case when SoldAsVacant = 'Yes' Then 'Y' when SoldAsVacant = 'No' then 'N' end
-----------------------------------------------------------------------------------------------------------------------------------------------------------

-- 4. Remove Duplicates
/*
ROW_NUMBER() function assigns a sequential number to each row in a result set, starting from 1. 
The number depends on the order and partition of the rows, which are specified by the OVER clause.
The row_num column will have the value 1 for the first row in each group, and will increase by 1 for each subsequent row in the same group. 
If the group has only one row, the row_num will be 1. If the group has more than one row, the row_num will be different for each row, depending on the order of the UniqueID column.
The row number increases only when the values of all the columns in the PARTITION BY clause are the same. If any of the values are different, the row number starts from 1 again.
*/

WITH RowNum AS(
Select *,
	ROW_NUMBER() OVER (
	PARTITION BY ParcelID,
				 PropertyAddress_Split,
				 PropertyCity,
				 OwnerState,
				 SalePrice,
				 SaleDateConverted,
				 LegalReference
				 ORDER BY
					UniqueID
					) row_numb

From PortfolioProject..Nashville_DataSet
--order by ParcelID
)
/* Select *
From RowNum
Where row_numb = 1 -- This will return unique values
Order by PropertyAddress  */

Select *
From RowNum
Where row_numb > 1 -- This will return duplicate values
Order by PropertyAddress
---------------------------------------------------------------------------------------------------------

-- Delete Unused Columns not recommended though but if you are 100% sure you will not need it in the future you can remove it but still it is not really recommended
Select *
From PortfolioProject..Nashville_DataSet


ALTER TABLE PortfolioProject..Nashville_DataSet
DROP COLUMN OwnerAddress, TaxDistrict, PropertyAddress, SaleDate










