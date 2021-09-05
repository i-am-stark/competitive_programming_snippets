/* Given are the heights of certain Buildings which lie adjacent to each other. Sunlight starts falling from the left side of the buildings. If there is a building of a certain Height, all the buildings to the right side of it having lesser heights cannot see the sun. The task is to find the total number of such buildings that receive sunlight. */
int main() {
	int t;
	scanf("%d", &t);
	while(t--){
	    int n;
        scanf("%d", &n);
    	int arr[n];
    	int c = 1;
    	for(int i = 0; i<n; i++){
    	    scanf("%d", &arr[i]);
    	}
    	int grt = arr[0];
    	for (int i = 1; i<n; i++){
    	    if(arr[i]>=grt){
    	        c++;
    	        grt = arr[i];
    	    }
    	}
    	printf("%d \n", c);
	}
	return 0;
}