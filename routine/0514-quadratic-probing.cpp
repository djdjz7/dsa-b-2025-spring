// http://cs101.openjudge.cn/2025sp_routine/17975/
#include <iostream>
#include <vector>
using std::cin;
using std::cout;
using std::endl;

class DeltaGenerator {
private:
  int num, multiplier;

public:
  DeltaGenerator() {
    num = 1;
    multiplier = 1;
  }
  void reset() {
    num = 1;
    multiplier = 1;
  }
  int next() {
    int val = num * num * multiplier;
    num += (multiplier - 1) / 2;
    multiplier *= -1;
    return val;
  }
};

int main() {
  DeltaGenerator generator;
  int n, k;
  cin >> n >> k;
  std::vector<int> nums(n), hashmap(k, -1), positions;
  for (int i = 0; i < n; i++) {
    cin >> nums[i];
  }
  for (int num : nums) {
    generator.reset();
    for (int delta = 0;; delta = generator.next()) {
      int pos = (num + delta) % k;
      if (pos < 0) {
        pos += k;
      }
      if (hashmap[pos] == -1 || hashmap[pos] == num) {
        hashmap[pos] = num;
        positions.push_back(pos);
        break;
      }
    }
  }
  bool first = true;
  for (int pos : positions) {
    if (!first) {
      cout << " ";
    }
    cout << pos;
    first = false;
  }
  cout << endl;
}