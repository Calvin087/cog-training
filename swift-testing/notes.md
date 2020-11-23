## First Principle (unit tests)

F. Fast unit tests
I. Independant
R. Repeatable - hardware independant
S. Self validating, no manual checks
T. Timely, thorough - edge cases etc

## TDD

Write tests first, then write business logic.

Red - write test that fails
Green - write biz logic that passes tests
Refactor - clean both test and biz logic
Repeat - ...

</br>

---------------------

</br>

## Tests in Xcode

- Make sure to delete UITests in the Targets section - causes a build fail❗
- **@testable import**❗
  - Don't forget to add the target test module to newly created test files.
- **Diamonds denote TESTS**
- Tests run in **Alphabetical Order**
- **sut** == system under test
- [List of XCTAssertions from Apple](https://developer.apple.com/documentation/xctest)

You can add tests to an existing project by selecting the top most project folder and using the + button at the bottom. Search for the test type you want.

</br>

---------------------

</br>

## Set Up - Tear Down

```swift

class Photo_appTests: XCTestCase {

    // globally shared info / data
    // Placing this in the set up with a +=1 will increment before every test.....
    static var countSomthing = 0

    // Runs ONE TIME only
    override class func setUpWithError() throws {
        super.setup()

        }

    // Runs before EACH test //
    override func setUpWithError() throws {

        }

    // Cleans up memory after EACH test //
    override func tearDownWithError() throws {

    }

    // Runs ONE TIME only
    override class func tearDownWithError() throws {
        super.tearDown()

    }
}

```

## addTearDownBlock

This is called once from within a test. Clean up and release resources. For example saving things to local storage then deleting them to save memory / space.

```swift

func testExample() throws {
    
    print("Something funny")
    
    addTearDownBlock {
        print("Tearing down beause I was called right here")

    }
}

```

</br>

---------------------

</br>

## Naming Tests

- As always name starts with **test**
- No Returns
- No Arguments

Good name Eg:

```swift

// func test<System under Test>_<Condition or State Change>_<Expected Result>
func testSignupFormModel_WhenInformationProvided_PasswordShouldMatchRepeatedPassword() {

}

```

</br>

---------------------

</br>

## Code Coverage 85%

It's generally agreed that the code base has around 85% coverage as 100% is challenging. It also doesn't mean that there are NO bugs, it just means that everything has been tested in some way.

How much of my code is covered by unit tests. This builds a report of coverage of tests.

- *Product -> Scheme -> Edit Scheme -> Test -> Options -> Coverage*

Open up **Report Navigator** to see the results

</br>

---------------------

</br>

## AAA Pattern

Arrange - variables, arrays, const, setup
Act - perform tests, invoke methods
Assert - check results

</br>

---------------------

</br>

## Debugging Failure Breakpoint

Next to the reports navigator there is a tab for breakpoint navigation. + button to use "Test Failure Breakpoint". Stops testing and takes me to the the assertion that failed.

Use step in and step over buttons at the bottom of the screen to go into that function and see the logic as it's happening.

### Checking tests that also use that unit
Once the assertion has been addressed. Check other tests that use that function.

- ^1 to show **Related Items**
- Test Callers
- Visit each of the tests.



</br>

---------------------

</br>

## Parallel Distributed Testing

Allows me to use multiple simulators to run more than 1 test at the same time. This can be changed in preferences on Genral tab.

- *Product -> Scheme -> Edit Scheme -> Test -> Info -> Tests/Options -> Execute if possible*

Provides addtional reports.

</br>

---------------------

</br>

## Example Work Flow

Tests drive the requirements for business logic...

- Create test file
- Write a long old name for a test method
- A.AA
- Set up a variable to be tested ```sut = className``` which doesn't exist.
- See error
- Go and create that CLASS
- import it then "build app to see changes"
- AA.A
- set up method to test
- see error
- go write the method on the new class etc etc

</br>

---------------------

</br>

## Insecure HTTP requests

- info.plist
- Add new line ```App transport security settings```
- ```Allow arbitrary loads``` = Yes

</br>

---------------------

</br>


### Accidently Adding Git, remove 

**Manual Delete**

Open Terminal and type

```
$ defaults write com.apple.finder AppleShowAllFiles TRUE
$ killall Finder
```

simply open the project in finder delete the .git and .gitignore from root/ (Where project file is present)