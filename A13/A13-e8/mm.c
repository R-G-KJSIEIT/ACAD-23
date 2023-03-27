#include <stdio.h>

int main()
{
	int osm,tm,tif,i,j,n,p[n],b,nb,inf[n];
	printf("This program has been created by Rishikesh Giridhar");
	printf("\nEnter total available Memory:");
	scanf("%d",&tm);
	printf("\nEnter amount of memory occupied by the OS: ");
	scanf("%d",&osm);
	printf("\nEnter number of processes: ");
	scanf("%d",&n);
	printf("\nEnter size of each block: ");
	scanf("%d",&b);
	nb=tm/b;
	tm-=osm;
	for(i=0;i<=n;i++) {
		printf("\nEnter required memory for process %d: ",i);
		scanf("%d",&p[i]);
	}
	for (i=0;i<=n;i++) {
		inf[i]=b-p[i];
		printf("\nprocess %d: \nmemory required:%d \n remaining memory:%d \n internal fragmentation:%d",i,p[i],tm,inf[i]);
		tm-=p[i];
	}
	for (i=0;i<=n;i++) {
		if (p[i]<b) {
			inf[i]=tm-p[i];
		}
		else if(p[i]==b) {
			continue;
		}
		else {
			printf("cannot allocate sorry");
		}
	}
	for (i=0;i<=n;i++) {
		tif+=inf[i];
	}
	printf("\nTotal internal fragmentation is:%d",tif);
	return 0;
}
