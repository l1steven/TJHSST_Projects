#include <iostream>
using namespace std;
#include <time.h>
#include <cmath>
#include <fstream>
#include <iomanip>
#include <vector>
#include <algorithm>
class Point
{
   public:
      double getR(); //gray value
      double getG(); //gradient
      double getB(); //angle
      double getBX();//X gradient
      double getBY();//y Gradient
      int getV();  //voting count using extend line
      int getID2(); //hysterisis value
      int getID();//non max value
      int getID3(); //non max+hysterisis
      int getID4(); //
      int getOR();  //real red
      int getOG();  //real green
      int getOB();  //real blue
      int getRad();
      int getVotes();
      void setVotes(int v); //number of radius votes
      void setRad(int ra);
      bool getCenter(); //candidate for coin center
      void setCenter(bool b);
      bool getCenter2(); //candidate for coin center with radius
      void setCenter2(bool b);
      bool getCircle(); //draw circle here
      void setCircle(bool b);
      bool getCircle2();//point on circle
      void setCircle2(bool b);
      int getCircle3();
      void setCircle3(int b); //classify which coin
      void setID4(int i4);
      void setID3(int i3);
      void setID2(int i2);
      void setID(int i);
      void setBX(double b1);
      void setBY(double b1);
      void setR(double r1);
      void setG(double g1);
      void setB(double b1);
      void setV(int v1);
      void setPoint(int r1, int g1, int b1);
      bool equals(Point p);
   private:
      double r,g,b, bx, by;
      int id, id2,id3,v,id4,ore,og,ob, rad;
      bool isCenter,isCenter2;
      bool circle,circle2;
      int circle3,votes;
};
void Point::setCenter(bool b)
{
   isCenter=b;
}
bool Point::getCenter()
{
   return isCenter;
}
int Point::getRad()
{
   return rad;
}
void Point::setRad(int ra)
{
   rad=ra;
}
int Point::getVotes()
{
   return votes;
}
void Point::setVotes(int v)
{
   votes=v;
}
void Point::setCenter2(bool b)
{
   isCenter2=b;
}
bool Point::getCenter2()
{
   return isCenter2;
}
void Point::setCircle(bool b)
{
   circle=b;
}
bool Point::getCircle()
{
   return circle;
}
void Point::setCircle2(bool b)
{
   circle2=b;
}
bool Point::getCircle2()
{
   return circle2;
}
void Point::setCircle3(int b)
{
   circle3=b;
}
int Point::getCircle3()
{
   return circle3;
}
void Point::setID(int i)
{
   id=i;
}
int Point::getID()
{
   return id;
}
void Point::setID2(int i2)
{
   id2=i2;
}
int Point::getID2()
{
   return id2;
}
void Point::setID3(int i3)
{
   id3=i3;
}
int Point::getID3()
{
   return id3;
}
void Point::setID4(int i4)
{
   id4=i4;
}
int Point::getID4()
{
   return id4;
}
void Point::setV(int v1)
{
   v=v1;
}
int Point::getV()
{
   return v;
}
void Point::setPoint(int r1,int g1,int b1)
{
   ore=r1;
   og=g1;
   ob=b1;
}
int Point::getOR()
{
   return ore;
}
int Point::getOB()
{
   return ob;
}
int Point::getOG()
{
   return og;
}
void Point::setR(double r1)
{
   r=r1;
}
void Point::setG(double g1)
{
   g=g1;
}
void Point::setB(double b1)
{
   b=b1;
}
void Point::setBY(double b1)
{
   by=b1;
}
void Point::setBX(double b1)
{
   bx=b1;
}
double Point::getR()
{
   return r;
}
double Point::getG()
{
   return g;
}
double Point::getB()
{
   return b;
}
double Point::getBX()
{
   return bx;
}
double Point::getBY()
{
   return by;
}
double rad(double degrees)
{
   return degrees*M_PI/180.0;
}
void circleHelper(int xc,int yx, int x, int y,vector<vector<Point>>& array,int dimy,int dimx,int mode,int& count)    //helper method to draw the circle
{
    using namespace std;
    /*int dimy=array.size();
    int dimx=array[0].size();*/
    //int xc=p.x;
    //int yx=p.y;
    /*if(xc+x<dimx && yx+y<dimy&& xc+x>=0 && yx+y>=0) array.at(xc+x).at(yx+y).setPoint(255,0,0);
    if(xc-x<dimx && yx+y<dimy&& xc-x>=0 && yx+y>=0) array.at(xc-x).at(yx+y).setPoint(255,0,0);
    if(xc+x<dimx && yx-y<dimy&& xc+x>=0 && yx-y>=0) array.at(xc+x).at(yx-y).setPoint(255,0,0);
    if(xc-x<dimx && yx-y<dimy&& xc-x>=0 && yx-y>=0) array.at(xc-x).at(yx-y).setPoint(255,0,0);
    if(xc+y<dimx && yx+x<dimy&& xc+y>=0 && yx+x>=0) array.at(xc+y).at(yx+x).setPoint(255,0,0);
    if(xc-y<dimx && yx+x<dimy&& xc-y>=0 && yx+x>=0) array.at(xc-y).at(yx+x).setPoint(255,0,0);
    if(xc+y<dimx && yx-x<dimy&& xc+y>=0 && yx-x>=0) array.at(xc+y).at(yx-x).setPoint(255,0,0);
    if(xc-y<dimx && yx-x<dimy&& xc-y>=0 && yx-x>=0) array.at(xc-y).at(yx-x).setPoint(255,0,0);*/
    if(mode==0)
    {
      if(xc+x<dimx && yx+y<dimy&& xc+x>=0 && yx+y>=0) array.at(xc+x).at(yx+y).setCircle(true);
      if(xc-x<dimx && yx+y<dimy&& xc-x>=0 && yx+y>=0) array.at(xc-x).at(yx+y).setCircle(true);
      if(xc+x<dimx && yx-y<dimy&& xc+x>=0 && yx-y>=0) array.at(xc+x).at(yx-y).setCircle(true);
      if(xc-x<dimx && yx-y<dimy&& xc-x>=0 && yx-y>=0) array.at(xc-x).at(yx-y).setCircle(true);
      if(xc+y<dimx && yx+x<dimy&& xc+y>=0 && yx+x>=0) array.at(xc+y).at(yx+x).setCircle(true);
      if(xc-y<dimx && yx+x<dimy&& xc-y>=0 && yx+x>=0) array.at(xc-y).at(yx+x).setCircle(true);
      if(xc+y<dimx && yx-x<dimy&& xc+y>=0 && yx-x>=0) array.at(xc+y).at(yx-x).setCircle(true);
      if(xc-y<dimx && yx-x<dimy&& xc-y>=0 && yx-x>=0) array.at(xc-y).at(yx-x).setCircle(true);
    }
    else if(mode==1)
    {
      if(xc+x<dimx && yx+y<dimy&& xc+x>=0 && yx+y>=0) array.at(xc+x).at(yx+y).setCircle2(true);
      if(xc-x<dimx && yx+y<dimy&& xc-x>=0 && yx+y>=0) array.at(xc-x).at(yx+y).setCircle2(true);
      if(xc+x<dimx && yx-y<dimy&& xc+x>=0 && yx-y>=0) array.at(xc+x).at(yx-y).setCircle2(true);
      if(xc-x<dimx && yx-y<dimy&& xc-x>=0 && yx-y>=0) array.at(xc-x).at(yx-y).setCircle2(true);
      if(xc+y<dimx && yx+x<dimy&& xc+y>=0 && yx+x>=0) array.at(xc+y).at(yx+x).setCircle2(true);
      if(xc-y<dimx && yx+x<dimy&& xc-y>=0 && yx+x>=0) array.at(xc-y).at(yx+x).setCircle2(true);
      if(xc+y<dimx && yx-x<dimy&& xc+y>=0 && yx-x>=0) array.at(xc+y).at(yx-x).setCircle2(true);
      if(xc-y<dimx && yx-x<dimy&& xc-y>=0 && yx-x>=0) array.at(xc-y).at(yx-x).setCircle2(true);
      if(xc+x<dimx && yx+y<dimy&& xc+x>=0 && yx+y>=0&&array.at(xc+x).at(yx+y).getCircle2()&&array.at(xc+x).at(yx+y).getID3()==1) count=count+1;
      if(xc-x<dimx && yx+y<dimy&& xc-x>=0 && yx+y>=0&&array.at(xc-x).at(yx+y).getCircle2()&&array.at(xc-x).at(yx+y).getID3()==1) count=count+1;
      if(xc+x<dimx && yx-y<dimy&& xc+x>=0 && yx-y>=0&&array.at(xc+x).at(yx-y).getCircle2()&&array.at(xc+x).at(yx-y).getID3()==1) count=count+1;
      if(xc-x<dimx && yx-y<dimy&& xc-x>=0 && yx-y>=0&&array.at(xc-x).at(yx-y).getCircle2()&&array.at(xc-x).at(yx-y).getID3()==1) count=count+1;
      if(xc+y<dimx && yx+x<dimy&& xc+y>=0 && yx+x>=0&&array.at(xc+y).at(yx+x).getCircle2()&&array.at(xc+y).at(yx+x).getID3()==1) count=count+1;
      if(xc-y<dimx && yx+x<dimy&& xc-y>=0 && yx+x>=0&&array.at(xc-y).at(yx+x).getCircle2()&&array.at(xc-y).at(yx+x).getID3()==1) count=count+1;
      if(xc+y<dimx && yx-x<dimy&& xc+y>=0 && yx-x>=0&&array.at(xc+y).at(yx-x).getCircle2()&&array.at(xc+y).at(yx-x).getID3()==1) count=count+1;
      if(xc-y<dimx && yx-x<dimy&& xc-y>=0 && yx-x>=0&&array.at(xc-y).at(yx-x).getCircle2()&&array.at(xc-y).at(yx-x).getID3()==1) count=count+1; 
    }
    else if(mode==2)
    {
       if(xc+x<dimx && yx+y<dimy&& xc+x>=0 && yx+y>=0) array.at(xc+x).at(yx+y).setCircle2(false);
    if(xc-x<dimx && yx+y<dimy&& xc-x>=0 && yx+y>=0) array.at(xc-x).at(yx+y).setCircle2(false);
    if(xc+x<dimx && yx-y<dimy&& xc+x>=0 && yx-y>=0) array.at(xc+x).at(yx-y).setCircle2(false);
    if(xc-x<dimx && yx-y<dimy&& xc-x>=0 && yx-y>=0) array.at(xc-x).at(yx-y).setCircle2(false);
    if(xc+y<dimx && yx+x<dimy&& xc+y>=0 && yx+x>=0) array.at(xc+y).at(yx+x).setCircle2(false);
    if(xc-y<dimx && yx+x<dimy&& xc-y>=0 && yx+x>=0) array.at(xc-y).at(yx+x).setCircle2(false);
    if(xc+y<dimx && yx-x<dimy&& xc+y>=0 && yx-x>=0) array.at(xc+y).at(yx-x).setCircle2(false);
    if(xc-y<dimx && yx-x<dimy&& xc-y>=0 && yx-x>=0) array.at(xc-y).at(yx-x).setCircle2(false);
    }
    else if(mode==3)
    {
      if(xc+x<dimx && yx+y<dimy&& xc+x>=0 && yx+y>=0) array.at(xc+x).at(yx+y).setCircle3(count);
      if(xc-x<dimx && yx+y<dimy&& xc-x>=0 && yx+y>=0) array.at(xc-x).at(yx+y).setCircle3(count);
      if(xc+x<dimx && yx-y<dimy&& xc+x>=0 && yx-y>=0) array.at(xc+x).at(yx-y).setCircle3(count);
      if(xc-x<dimx && yx-y<dimy&& xc-x>=0 && yx-y>=0) array.at(xc-x).at(yx-y).setCircle3(count);
      if(xc+y<dimx && yx+x<dimy&& xc+y>=0 && yx+x>=0) array.at(xc+y).at(yx+x).setCircle3(count);
      if(xc-y<dimx && yx+x<dimy&& xc-y>=0 && yx+x>=0) array.at(xc-y).at(yx+x).setCircle3(count);
      if(xc+y<dimx && yx-x<dimy&& xc+y>=0 && yx-x>=0) array.at(xc+y).at(yx-x).setCircle3(count);
      if(xc-y<dimx && yx-x<dimy&& xc-y>=0 && yx-x>=0) array.at(xc-y).at(yx-x).setCircle3(count);
    }

    
}
    
void drawCircle(int cx, int cy, int r, vector<vector<Point>>& array,int dimx,int dimy, int mode,int&count) //method to draw circle given center and radius
{
    //int cx=p.x;
    //int cy=p.y;
    int xmax=(int)(r*0.70710678);
    int y=r;
    int y2=r*r;
    int ty=(2*r)-1;
    int y2_new=y2;
    for(int x=0;x<=xmax;x++)
    {
        if((y2-y2_new)>=ty)
        {
            y2=y2-ty;
            y=y-1;
            ty=ty-2;
        }
        circleHelper(cx,cy,x,y,array,dimx,dimy,mode,count);

        y2_new =y2_new -(2 * x) + 3;
        //cout<<" hi ";
    }
}
void drawLine(int x1, int y1, int x2, int y2,vector<vector<Point>>& array) //draw line using bresenhams algorithm
{
    using namespace std;
    //cout<<x1<<" "<<y1<<" "<<x2<<" "<<y2;
   /* if(abs(y2-y1)>abs(x2-x1))
    {
        swap(x1,y1);
        swap(x2,y2);    
    }*/
    int dy=y2-y1;
    int dx=x2-x1;
    int e=abs(dy)-abs(dx);
    int xinc=1;
    int yinc=1;
    int i=x1;
    int j=y1;
    int i2=x2;
    int j2=y2;
    if(dy<0&&dx<0)
    {
        /*yinc=-1;
        j=y2;
        j2=y1;
        xinc=-1;
        i=x2;
        i2=x1;*/
        swap(x2,x1);
        swap(y1,y2);
        swap(j,j2);
        swap(i,i2);
        dy=dy*-1;
        dx=dx*-1;
    }
    else if (dy<0)
    {
        yinc=-1;
    }
    else if (dx<0)
    {
        xinc=-1;
    }
    else{}

    if(abs(dy)<abs(dx))
    {
    
        while(i!=i2)
        {
            array[i][j].setID4(1);
            //cout<<" "<<i<<" "<<j;
            array[i][j].setV(array[i][j].getV()+1);
            if(e>=0)
            {
                j=j+yinc;
                e=e-abs(dx);
            }
            i=i+xinc;
            e=e+abs(dy);
            //cout<<i<<" "<<j;
        }
    }
    else
    {
        e=abs(dx)-abs(dy);
        while(j!=j2)
        {
            array[i][j].setID4(1);
            array[i][j].setV(array[i][j].getV()+1);
            if(e>=0)
            {
                i=i+xinc;
                e=e-abs(dy);
            }
            j=j+yinc;
            e=e+abs(dx);
            //cout<<i<<" "<<j;
        }
    }
    
}
void extendLine2(double i, double j,double xSlope,double ySlope,vector<vector<Point>>& array,double dimx, double dimy)
{
   swap(xSlope,ySlope);
   ySlope=ySlope*-1;
   int jj = j;
   int ii = i;
   while(ii + ySlope >= 0 && ii + ySlope< dimy && jj + xSlope>= 0 && jj + xSlope < dimx){
      //votes[ii][jj] = votes[ii][jj] + 1;
      ii = ii + ySlope;
      jj = jj + xSlope;
   }
   int jjj = j;
   int iii = i;
   while(iii - ySlope >= 0 && iii -ySlope< dimy && jjj - xSlope>= 0 && jjj - xSlope < dimx){
      //votes[ii][jj] = votes[iii][jjj] + 1;
      iii = iii - ySlope;
      jjj = jjj - xSlope;
   }
   drawLine(ii,jj,iii,jjj,array);
}
void extendLine(double x1, double y1,double angle,vector<vector<Point>>& array,double dimy, double dimx)
{
   //double slope=(y2-y1)/(x2-x1);
   
   double slope;
   bool b=true;
   if(abs(angle)>(3*M_PI/4) || abs(angle)<(M_PI/4))
   {
      slope=tan(angle);
   }
   else
   {
      slope=1/tan(angle);
      b=false;
   }
   cout<<slope<<" ";
   double xdown=x1-0;
   double ydown=y1-0;
   double xup=x1-0;
   double yup=y1-0;
   if(b)
   {
      while(xup<dimx-2 && xup>1 && yup<dimy && yup>=0) //create two endpoints which contain the centroid, have the calculated slope, and go to the edges
      {
         xup=xup-1;
         yup=yup-slope;
      }
      while(xdown<dimx-2 && xdown>1 && ydown<dimy && ydown>=0)
      {
         xdown=xdown+1;
         ydown=ydown+slope;
      }
      if(yup>=dimy) yup=yup-slope;
      if(yup<0) yup=yup+slope;
      if(ydown>=dimy) ydown=ydown-slope;
      if(ydown<0) ydown=ydown+slope; 
   }
   else
   {
      while(yup<dimy-2 && yup>1 && xup<dimx && xup>=0) //create two endpoints which contain the centroid, have the calculated slope, and go to the edges
      {
         yup=yup-1;
         xup=xup-slope;
      }
      while(ydown<dimy-2 && ydown>1 && xdown<dimx && xdown>=0)
      {
         ydown=ydown+1;
         xdown=xdown+slope;
      }
      if(xup>=dimx) xup=xup-slope;
      if(xup<0) xup=xup+slope;
      if(xdown>=dimx) xdown=xdown-slope;
      if(xdown<0) xdown=xdown+slope; 
   }
   
   drawLine((int)xdown,(int)ydown,(int)xup,(int)yup,array);
}
void part2()
{
   vector<vector<Point>> points;
   ifstream ifs;
   ifs.open("image.ppm",ios_base::in|ios::binary);
   string first;
   int xdim,ydim,r,g,b;
   ifs>>first>>xdim>>ydim>>r;
   for(int i=0;i<ydim;i++)
   {
      vector<Point> v;
      points.push_back(v);
   }
   int count=0;
   while(ifs>>r>>g>>b)
   {
      Point p;
      p.setPoint(r,g,b);
      int avg=(int)((r+g+b)/3);
      p.setR(avg);
      points.at(count/xdim).push_back(p); //-1 0 1 -2 0 2 -1 0 1
      count++;
   }  
   /*ofstream ofs("imageg.ppm", ios_base::out | ios_base::binary);   //create ppm file with specified information
   ofs << "P6" << endl << xdim << ' ' << ydim << endl << "255" << endl;
   //auto array=new int[dimx][dimy];
   for(int i=0;i<ydim;i++)
   {
      for(int j=0;j<xdim;j++)
      {
         Point p=points.at(i).at(j);
         ofs<<(char)p.getR()<<(char)p.getR()<<(char)p.getR();
      }
   }*/
   for(int i=1;i<ydim-1;i++)
   {
      for(int j=1;j<xdim-1;j++)
      {
         int newx1=(-1*points.at(i-1).at(j-1).getR())+(-2*points.at(i).at(j-1).getR())+(-1*points.at(i+1).at(j-1).getR());
         int newx2=(1*points.at(i-1).at(j+1).getR())+(2*points.at(i).at(j+1).getR())+(1*points.at(i+1).at(j+1).getR());
         int newy1=(1*points.at(i-1).at(j-1).getR())+(2*points.at(i-1).at(j).getR())+(1*points.at(i-1).at(j+1).getR());
         int newy2=(-1*points.at(i+1).at(j-1).getR())+(-2*points.at(i+1).at(j).getR())+(-1*points.at(i+1).at(j+1).getR());
         points.at(i).at(j).setG(hypot(newx1+newx2,newy1+newy2));
         points.at(i).at(j).setB(atan2(newy2+newy1,newx2+newx1));
         points.at(i).at(j).setBX(newx1+newx2);
         points.at(i).at(j).setBY(newy1+newy2);
      }
   }
   for(int i=0;i<ydim;i++)
   {
      for(int j=0;j<xdim;j++)
      {
         if(i==0||j==0||i==ydim-1||j==xdim-1)
         {
            points.at(i).at(j).setID(0);
         }
         else
         {
            double angle=points.at(i).at(j).getB();
            double g=points.at(i).at(j).getG();
            if( (angle>rad(-157.5)&&angle<=rad(-112.5)) || (angle>rad(22.5)&&angle<=rad(67.5)) )
            {
               if( (g>points.at(i+1).at(j-1).getG()) && (g>points.at(i-1).at(j+1).getG()))
               {
                  points.at(i).at(j).setID(1);
               }
               else
               {
                  points.at(i).at(j).setID(0);
               }  
            }
            else if((angle>rad(-112.5)&&angle<=rad(-67.5))||(angle>rad(67.5)&&angle<=rad(112.5)))
            {
               if( (g>points.at(i+1).at(j).getG()) && (g>points.at(i-1).at(j).getG()))
               {
                  points.at(i).at(j).setID(1);
               }
               else
               {
                  points.at(i).at(j).setID(0);
               }  
            }
            else if((angle>rad(-67.5)&&angle<=rad(-22.5))||(angle>rad(112.5)&&angle<=rad(157.5)))
            {
               if( (g>points.at(i-1).at(j-1).getG()) && (g>points.at(i+1).at(j+1).getG()))
               {
                  points.at(i).at(j).setID(1);
               }
               else
               {
                  points.at(i).at(j).setID(0);
               }  
            }
            else
            {           
               if( (g>points.at(i).at(j-1).getG()) && (g>points.at(i).at(j+1).getG()))
               {
                  points.at(i).at(j).setID(1);
               }
               else
               {
                  points.at(i).at(j).setID(0);
               }  
            }

         }
         

      }
   }
   
   double tlow=100;
   double thigh=160;
   for(int i=0;i<ydim;i++)
   {
      for(int j=0;j<xdim;j++)
      {
         if(points.at(i).at(j).getG()<tlow)
         {
            points.at(i).at(j).setID2(0);
         }
         else if(points.at(i).at(j).getG()>thigh)
         {
            points.at(i).at(j).setID2(2);
         }
         else
         {
            points.at(i).at(j).setID2(1);
         }
         
      }
   }
   for(int i=1;i<ydim-1;i++)
   {
      for(int j=1;j<xdim-1;j++)
      {
         if(points.at(i).at(j).getID2()==1)
         {
            if(points.at(i-1).at(j-1).getID2()==2||
               points.at(i-1).at(j).getID2()==2||
               points.at(i-1).at(j+1).getID2()==2||
               points.at(i).at(j-1).getID2()==2||
               points.at(i).at(j+1).getID2()==2||
               points.at(i+1).at(j-1).getID2()==2||
               points.at(i+1).at(j).getID2()==2||
               points.at(i+1).at(j+1).getID2()==2)
            {
               points.at(i).at(j).setID2(2);
            }
            /*else
            {
               points.at(i).at(j).setR(0);
            }*/
            
               
         }
      }
   }
   for(int i=ydim-2;i>1;i--)
   {
      for(int j=xdim-2;j>1;j--)
      {
         if(points.at(i).at(j).getID2()==1)
         {
            if(points.at(i-1).at(j-1).getID2()==2||
               points.at(i-1).at(j).getID2()==2||
               points.at(i-1).at(j+1).getID2()==2||
               points.at(i).at(j-1).getID2()==2||
               points.at(i).at(j+1).getID2()==2||
               points.at(i+1).at(j-1).getID2()==2||
               points.at(i+1).at(j).getID2()==2||
               points.at(i+1).at(j+1).getID2()==2)
            {
               points.at(i).at(j).setID2(2);
            }
            /*else
            {
               points.at(i).at(j).setR(0);
            }*/
            
               
         }
      }
   }
   for(int i=1;i<ydim-1;i++)
   {
      for(int j=1;j<xdim-1;j++)
      {
         if(points.at(i).at(j).getID2()==1)
         {
            points.at(i).at(j).setID2(0);
         }
            
               
         
      }
   }
   for(int i=0;i<ydim;i++)
   {
      for(int j=0;j<xdim;j++)
      {
         Point p=points.at(i).at(j);
         if(p.getID2()==0||p.getID()==0)
         {
            points.at(i).at(j).setID3(0);
         }
         else
         {
            //ofs<<(char)(int)p.getG()<<(char)(int)p.getG()<<(char)(int)p.getG();
            points.at(i).at(j).setID3(1);
         }
         points.at(i).at(j).setV(0);
         points.at(i).at(j).setID4(0);
         points.at(i).at(j).setCenter(false);
         points.at(i).at(j).setCircle(false);
         points.at(i).at(j).setCircle2(false);
         points.at(i).at(j).setCircle3(0);
         points.at(i).at(j).setCenter2(false);
         points.at(i).at(j).setRad(false);
         points.at(i).at(j).setVotes(0);

      }
   }
   ofstream ofs3("imagef.ppm", ios_base::out | ios_base::binary);   //create ppm file with specified information
   ofs3 << "P3" << endl << xdim << ' ' << ydim << endl << "1" << endl;
   //auto array=new int[dimx][dimy];
   for(int i=0;i<ydim;i++)
   {
      for(int j=0;j<xdim;j++)
      {
         Point p=points.at(i).at(j);
         if(p.getID3()==0)
         {
            ofs3<<0<<" "<<0<<" "<<0<<" ";
         }
         else
         {
            //ofs<<(char)(int)p.getG()<<(char)(int)p.getG()<<(char)(int)p.getG();
            ofs3<<1<<" "<<1<<" "<<1<<" ";
         }
         ofs3<<endl;
      }
   }
   for(int i=0;i<ydim;i++)
   {
      for(int j=0;j<xdim;j++)
      {
         if(points.at(i).at(j).getID3()==1)
         {
            int gcd=__gcd((int)points.at(i).at(j).getBX(),(int)points.at(i).at(j).getBY());
            extendLine2(i,j,points.at(i).at(j).getBY()/gcd,points.at(i).at(j).getBX()/gcd,points,xdim,ydim);
         }
      }
   }
   //extendLine2(100,100,1,1,points,xdim,ydim);
   int max=0;
   
   for(int i=0;i<ydim;i++)
   {
      for(int j=0;j<xdim;j++)
      {
         if(points.at(i).at(j).getV()>max)
         {
            max=points.at(i).at(j).getV();
         }
         /*if(points.at(i).at(j).getV()>=thresh)
         {
            points.at(i).at(j).setCenter(true);
            
         }*/
      }
   }
   int thresh=50;
   for(int i=0;i<ydim;i++)
   {
      for(int j=0;j<xdim;j++)
      {
         
         if(points.at(i).at(j).getV()>=thresh)
         {
            points.at(i).at(j).setCenter(true);
            
         }
      }
   }
   //extendLine(100,100,0,points,xdim,ydim);
   //cout<<max;
   //string maxs=""
   ofstream ofs2("imagev.ppm", ios_base::out | ios_base::binary);   //create ppm file with specified information
   ofs2 << "P3" << endl << xdim << ' ' << ydim << endl << to_string(max) << endl;
   //auto array=new int[dimx][dimy];
   for(int i=0;i<ydim;i++)
   {
      for(int j=0;j<xdim;j++)
      {
         Point p=points.at(i).at(j);
         /*if(p.getID4()==0)
         {
            ofs2<<0<<" "<<0<<" "<<0<<" ";
         }
         else
         {
            //ofs<<(char)(int)p.getG()<<(char)(int)p.getG()<<(char)(int)p.getG();
            ofs2<<1<<" "<<1<<" "<<1<<" ";
         }
         ofs2<<endl;*/
         //cout<<p.getV()<<" ";
         //if(p.getV()>(int)(max/2))
         ofs2<<p.getV()<<" "<<p.getV()<<" "<<p.getV()<<" ";
         /*else
         {
            ofs2<<0<<" "<<0<<" "<<0<<" ";
         }*/
         
         ofs2<<endl;
      }
   }
   // ofstream ofs4("imageCC.ppm", ios_base::out | ios_base::binary);   //create ppm file with specified information
   // ofs4 << "P3" << endl << xdim << ' ' << ydim << endl << 255 << endl;
   // //auto array=new int[dimx][dimy];
   // for(int i=0;i<ydim;i++)
   // {
   //    for(int j=0;j<xdim;j++)
   //    {
   //       Point p=points.at(i).at(j);
   //       int useless=0;
   //       if(p.getCenter())
   //       {
   //          //cout<<" "<<i<<" "<<j;
   //          //drawCircle(i,j,6,points,xdim,ydim);
   //          drawCircle(i,j,5,points,xdim,ydim,0,useless);
   //          //cout<<" "<<xdim<<" "<<ydim;
   //          drawCircle(i,j,4,points,xdim,ydim,0,useless);
   //          drawCircle(i,j,3,points,xdim,ydim,0,useless);
   //          drawCircle(i,j,2,points,xdim,ydim,0,useless);
   //          drawCircle(i,j,1,points,xdim,ydim,0,useless);
   //       }
   //       /*if(p.getCircle())
   //       {
   //          ofs4<<255<<" "<<0<<" "<<0<<" ";
   //          cout<<" h ";
   //       }
   //       else
   //       {
   //          ofs4<<p.getOR()<<" "<<p.getOG()<<" "<<p.getOB()<<" ";
   //       }
   //       ofs4<<endl;*/
   //    }
   // }
   // for(int i=0;i<ydim;i++)
   // {
   //    for(int j=0;j<xdim;j++)
   //    {
   //       Point p=points.at(i).at(j);
   //       if(p.getCircle())
   //       {
   //          ofs4<<255<<" "<<0<<" "<<0<<" ";
   //          //cout<<" h ";
   //       }
   //       else
   //       {
   //          ofs4<<p.getOR()<<" "<<p.getOG()<<" "<<p.getOB()<<" ";
   //       }
   //       ofs4<<endl;
      
   //    }
   // }
   int minRad=80;
   int maxRad=120;
   int diff=maxRad-minRad;
   //int radiusVotes[diff+1];
   int threshold2=130;
   vector<Point*> centers;
   vector<int> coords;
   for(int i=0;i<ydim;i++)
   {
      for(int j=0;j<xdim;j++)
      {
         if(points[i][j].getCenter())
         {
            int radiusVotes[diff+1];
            for(int k=minRad;k<=maxRad;k++)
            {
               int countss=0;
               drawCircle(i,j,k,points,xdim,ydim,1,countss);
               radiusVotes[k-minRad]=countss;
               drawCircle(i,j,k,points,xdim,ydim,2,countss);
            }
            int maxRadius=0;
            int radi=0;
            bool check=false;
            for(int ra=0;ra<=diff;ra++)
            {
               //cout<<radiusVotes[r]<<" ";
               if(radiusVotes[ra]>=threshold2)
               {
                  // //drawCircle(i,j,ra+minRad,points,xdim,ydim,3,maxRad);
                  // if(ra+minRad>maxRadius)
                  // {
                  //    maxRadius=ra+minRad;
                  // }
                  // //Point* p=points.at(i).at(j);
                  // centers.push_back(&points.at(i).at(j));
                  // coords.push_back(i);
                  // coords.push_back(j);
                  points.at(i).at(j).setCenter2(true);
                  check=true;
                  if(radiusVotes[ra]>maxRadius)
                  {
                     maxRadius=radiusVotes[ra];
                     radi=ra+minRad;
                  }
               }
            }
            if(check)
            {
               centers.push_back(&points.at(i).at(j));
               coords.push_back(i);
               coords.push_back(j);
               points.at(i).at(j).setRad(radi);
               points.at(i).at(j).setVotes(maxRadius);
            }
         }
      }   
   }
   for(int i=0;i<centers.size();i++)
   {
      for(int j=0;j<centers.size();j++)
      {
         if(i!=j)
         {
            if(centers.at(i)->getCenter2())
            {
               if(hypot(coords.at(i*2)-coords.at(j*2),coords.at(i*2+1)-coords.at(j*2+1))<40)
               {
                  if(centers.at(i)->getVotes()>=centers.at(j)->getVotes())
                     centers.at(j)->setCenter2(false);
                  else
                  {
                     centers.at(i)->setCenter2(false);
                  }
                  
               }
            }
         }
      }
   }
   int quarters=0;
   int dimes=0;
   int pennys=0;
   int nickels=0;
   for(int i=0;i<ydim;i++)
   {
      for(int j=0;j<xdim;j++)
      {
         Point p=points.at(i).at(j);
         if(p.getCenter2())
         {
            int color=0;
            if((p.getOR()-p.getOG()>10&&p.getOR()-p.getOB()>10))
            {
               color=1; //penny
               pennys++;
               
            }
            else if(p.getRad()>104)
            {
               color=4; //quarter
               quarters++;
               
            }
            else if(p.getRad()<95)
            {
               color=2; //dime
               dimes++;
            }
            else
            {
               color=3; //nickel
               nickels++;
            }
            drawCircle(i,j,p.getRad(),points,xdim,ydim,3,color);
         }
         
      }
   }
   ofstream ofs5("coins.ppm", ios_base::out | ios_base::binary);   //create ppm file with specified information
   ofs5 << "P3" << endl << xdim << ' ' << ydim << endl << 255 << endl;
   //auto array=new int[dimx][dimy];
   
   for(int i=0;i<ydim;i++)
   {
      for(int j=0;j<xdim;j++)
      {
         Point p=points.at(i).at(j);
         if(p.getCircle3()==1)
         {
            ofs5<<255<<" "<<0<<" "<<0<<" ";
            
         }
         else if(p.getCircle3()==3)
         {
            ofs5<<128<<" "<<0<<" "<<128<<" ";
         }
         else if(p.getCircle3()==2)
         {
            ofs5<<0<<" "<<0<<" "<<255<<" ";
         }
         else if(p.getCircle3()==4)
         {
            ofs5<<0<<" "<<255<<" "<<0<<" ";
         }
         else if(p.getID3()==1)
         {
            ofs5<<255<<" "<<255<<" "<<255<<" ";
         }
         else
         {
            ofs5<<0<<" "<<0<<" "<<0<<" ";
         }
         ofs5<<endl;
      }
   }
   double sum=0.25*quarters+0.1*dimes+0.05*nickels+0.01*pennys;
   ofstream ofs6("results.txt");

   ofs6<<quarters<<" quarters, "<<dimes<<" dimes, "<<nickels<<" nickels, "<<pennys<<" pennys, total sum: $"<<sum;

   ofs6.close();
   cout<<quarters<<" quarters, "<<dimes<<" dimes, "<<nickels<<" nickels, "<<pennys<<" pennys, total sum: $"<<sum;
}

int main()
{
   part2();
   return EXIT_SUCCESS;
}