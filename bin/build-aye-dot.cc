#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <string>
#include <cstring>
#include <sstream>
#include <cmath>

using namespace std;

map<string, int> rootIndex;
vector<string> roots;
float rootReff[2000][2000], rootCos[2000][2000];

struct Quran {
	int roots[114][300][200][10];
	int sureSize, ayeSize[114], wordSize[114][300], subwordSize[114][300][200];

	Quran() {
		memset(roots, 0, sizeof roots);
	}

	void load() {
		const char* fname = "../data/quran-roots.dat";
		ifstream fi(fname);
		cerr << "File opened " << fname << endl;
		string r;
		for (int s, a, w, sw; fi >> s >> a >> w >> sw >> r; ) {
			roots[s-1][a-1][w-1][sw-1] = rootIndex[r];
			sureSize = max(sureSize, s);
			ayeSize[s-1] = max(ayeSize[s-1], a);
			wordSize[s-1][a-1] = max(wordSize[s-1][a-1], w);
			subwordSize[s-1][a-1][w-1] = max(subwordSize[s-1][a-1][w-1], sw);
		}
	}
};

void loadRootReff() {
	const char* fname = "../data/root-reff.dat";
	ifstream fi(fname);
	string rootL;
	getline(fi, rootL);
	istringstream rootLss(rootL.c_str());
	for (string r; rootLss >> r; ) {
		rootIndex[r] = roots.size();
		roots.push_back(r);
	}
	cerr << "Roots: " << roots.size() << endl;
	for (int i=0; i<roots.size(); i++)
		for (int j=0; j<roots.size(); j++) {
			fi >> rootReff[i][j];
			rootCos[i][j] = 1.0/sqrt(1.0+rootReff[i][j]);
		}
}

int main() {
	Quran quran;
	quran.load();
	cerr << "Quran loaded " << endl;
	loadRootReff();
	cerr << "Reff loaded " << " " << rootReff[1][0] << " " << rootCos[1][0] << endl;

	vector<vector<vector<int> > > ayeRoots;
	for (int s = 0; s < quran.sureSize; s++) {
		ayeRoots.push_back(vector<vector<int> >());
		for (int a = 0; a < quran.ayeSize[s]; a++) {
			ayeRoots[s].push_back(vector<int>());
			for (int w=0; w<quran.wordSize[s][a]; w++)
				for (int sw=0; sw<quran.subwordSize[s][a][w]; sw++)
					ayeRoots[s][a].push_back(quran.roots[s][a][w][sw]);
		}
	}


	for (int s = 0; s < quran.sureSize; s++) {
		//cerr << s << " " << quran.ayeSize[s] << endl;
		for (int a = 0; a < quran.ayeSize[s]; a++) {
			cout << s+1 << ":" << a+1 << " ";
		}
	}
	cout << endl;
	for (int s = 0; s < quran.sureSize; s++) {
		cerr << "D " << s  << endl;
		for (int a = 0; a < quran.ayeSize[s]; a++) {
			for (int s2=0; s2<quran.sureSize; s2++)
				for (int a2=0; a2<quran.ayeSize[s2]; a2++) {
					double d = 0;
					for (int r1=0; r1<ayeRoots[s][a].size(); r1++)
						for (int r2=0; r2<ayeRoots[s2][a2].size(); r2++)
							d += rootCos[r1][r2];
					//cout << s << " " << a << " " << s2 << " " << a2 << " " << d << endl;
					cout << d << " ";
				}
			cout << endl;
		}
	}
	return 0;
}
