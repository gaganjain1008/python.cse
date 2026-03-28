#include <iostream>
using namespace std;

class Employee {
private:
    string name, department;
    int empID;
    float basicSalary, DA, HRA, TA, LIC, netSalary;

public:
    void input() {
        cout << "Enter Employee Name: ";
        cin.ignore();
        getline(cin, name);

        cout << "Enter Employee ID: ";
        cin >> empID;

        cout << "Enter Department: ";
        cin.ignore();
        getline(cin, department);

        cout << "Enter Basic Salary: ";
        cin >> basicSalary;
    }

    void calculate() {
        DA = 0.92 * basicSalary;
        HRA = 0.58 * basicSalary;
        TA = 0.30 * basicSalary;
        LIC = 500;

        netSalary = basicSalary + DA + HRA + TA - LIC;
    }

    void display() {
        cout << "\n--- Employee Details ---\n";
        cout << "Name: " << name << endl;
        cout << "Employee ID: " << empID << endl;
        cout << "Department: " << department << endl;
        cout << "Basic Salary: " << basicSalary << endl;
        cout << "DA: " << DA << endl;
        cout << "HRA: " << HRA << endl;
        cout << "TA: " << TA << endl;
        cout << "LIC Deduction: " << LIC << endl;
        cout << "Net Salary: " << netSalary << endl;
    }
};

int main() {
    Employee e;
    e.input();
    e.calculate();
    e.display();
    return 0;
}
