CXX = clang++
CXXFLAGS = -std=c++17
TARGET = $(patsubst %.cpp,%,$(wildcard day*.cpp))

# Default rule: Build specific day (e.g., make day1)
%: %.cpp
	$(CXX) $(CXXFLAGS) -o $@ $<

# Clean rule: Remove all executables (e.g., day1, day2, etc.)
clean:
	rm -f $(TARGET)