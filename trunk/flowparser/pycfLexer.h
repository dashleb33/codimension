/** \file
 *  This C header file was generated by $ANTLR version 3.2 Sep 23, 2009 12:02:23
 *
 *     -  From the grammar source file : pycf.g
 *     -                            On : 2014-05-20 19:56:58
 *     -                 for the lexer : pycfLexerLexer *
 * Editing it, at least manually, is not wise. 
 *
 * C language generator and runtime by Jim Idle, jimi|hereisanat|idle|dotgoeshere|ws.
 *
 *
 * The lexer pycfLexer has the callable functions (rules) shown below,
 * which will invoke the code for the associated rule in the source grammar
 * assuming that the input stream is pointing to a token/text stream that could begin
 * this rule.
 * 
 * For instance if you call the first (topmost) rule in a parser grammar, you will
 * get the results of a full parse, but calling a rule half way through the grammar will
 * allow you to pass part of a full token stream to the parser, such as for syntax checking
 * in editors and so on.
 *
 * The parser entry points are called indirectly (by function pointer to function) via
 * a parser context typedef ppycfLexer, which is returned from a call to pycfLexerNew().
 *
 * As this is a generated lexer, it is unlikely you will call it 'manually'. However
 * the methods are provided anyway.
 * * The methods in ppycfLexer are  as follows:
 *
 *  -  void      ppycfLexer->T__98(ppycfLexer)
 *  -  void      ppycfLexer->T__99(ppycfLexer)
 *  -  void      ppycfLexer->T__100(ppycfLexer)
 *  -  void      ppycfLexer->T__101(ppycfLexer)
 *  -  void      ppycfLexer->T__102(ppycfLexer)
 *  -  void      ppycfLexer->T__103(ppycfLexer)
 *  -  void      ppycfLexer->T__104(ppycfLexer)
 *  -  void      ppycfLexer->T__105(ppycfLexer)
 *  -  void      ppycfLexer->T__106(ppycfLexer)
 *  -  void      ppycfLexer->T__107(ppycfLexer)
 *  -  void      ppycfLexer->T__108(ppycfLexer)
 *  -  void      ppycfLexer->T__109(ppycfLexer)
 *  -  void      ppycfLexer->T__110(ppycfLexer)
 *  -  void      ppycfLexer->T__111(ppycfLexer)
 *  -  void      ppycfLexer->T__112(ppycfLexer)
 *  -  void      ppycfLexer->T__113(ppycfLexer)
 *  -  void      ppycfLexer->T__114(ppycfLexer)
 *  -  void      ppycfLexer->T__115(ppycfLexer)
 *  -  void      ppycfLexer->T__116(ppycfLexer)
 *  -  void      ppycfLexer->T__117(ppycfLexer)
 *  -  void      ppycfLexer->T__118(ppycfLexer)
 *  -  void      ppycfLexer->T__119(ppycfLexer)
 *  -  void      ppycfLexer->T__120(ppycfLexer)
 *  -  void      ppycfLexer->T__121(ppycfLexer)
 *  -  void      ppycfLexer->T__122(ppycfLexer)
 *  -  void      ppycfLexer->T__123(ppycfLexer)
 *  -  void      ppycfLexer->T__124(ppycfLexer)
 *  -  void      ppycfLexer->T__125(ppycfLexer)
 *  -  void      ppycfLexer->T__126(ppycfLexer)
 *  -  void      ppycfLexer->T__127(ppycfLexer)
 *  -  void      ppycfLexer->T__128(ppycfLexer)
 *  -  void      ppycfLexer->T__129(ppycfLexer)
 *  -  void      ppycfLexer->T__130(ppycfLexer)
 *  -  void      ppycfLexer->T__131(ppycfLexer)
 *  -  void      ppycfLexer->T__132(ppycfLexer)
 *  -  void      ppycfLexer->T__133(ppycfLexer)
 *  -  void      ppycfLexer->T__134(ppycfLexer)
 *  -  void      ppycfLexer->T__135(ppycfLexer)
 *  -  void      ppycfLexer->T__136(ppycfLexer)
 *  -  void      ppycfLexer->T__137(ppycfLexer)
 *  -  void      ppycfLexer->T__138(ppycfLexer)
 *  -  void      ppycfLexer->T__139(ppycfLexer)
 *  -  void      ppycfLexer->T__140(ppycfLexer)
 *  -  void      ppycfLexer->T__141(ppycfLexer)
 *  -  void      ppycfLexer->T__142(ppycfLexer)
 *  -  void      ppycfLexer->T__143(ppycfLexer)
 *  -  void      ppycfLexer->T__144(ppycfLexer)
 *  -  void      ppycfLexer->T__145(ppycfLexer)
 *  -  void      ppycfLexer->T__146(ppycfLexer)
 *  -  void      ppycfLexer->T__147(ppycfLexer)
 *  -  void      ppycfLexer->T__148(ppycfLexer)
 *  -  void      ppycfLexer->T__149(ppycfLexer)
 *  -  void      ppycfLexer->T__150(ppycfLexer)
 *  -  void      ppycfLexer->T__151(ppycfLexer)
 *  -  void      ppycfLexer->T__152(ppycfLexer)
 *  -  void      ppycfLexer->T__153(ppycfLexer)
 *  -  void      ppycfLexer->T__154(ppycfLexer)
 *  -  void      ppycfLexer->T__155(ppycfLexer)
 *  -  void      ppycfLexer->T__156(ppycfLexer)
 *  -  void      ppycfLexer->T__157(ppycfLexer)
 *  -  void      ppycfLexer->T__158(ppycfLexer)
 *  -  void      ppycfLexer->T__159(ppycfLexer)
 *  -  void      ppycfLexer->T__160(ppycfLexer)
 *  -  void      ppycfLexer->T__161(ppycfLexer)
 *  -  void      ppycfLexer->STRINGLITERAL(ppycfLexer)
 *  -  void      ppycfLexer->STRINGPREFIX(ppycfLexer)
 *  -  void      ppycfLexer->SHORTSTRING(ppycfLexer)
 *  -  void      ppycfLexer->LONGSTRING(ppycfLexer)
 *  -  void      ppycfLexer->BYTESLITERAL(ppycfLexer)
 *  -  void      ppycfLexer->BYTESPREFIX(ppycfLexer)
 *  -  void      ppycfLexer->SHORTBYTES(ppycfLexer)
 *  -  void      ppycfLexer->LONGBYTES(ppycfLexer)
 *  -  void      ppycfLexer->TRIAPOS(ppycfLexer)
 *  -  void      ppycfLexer->TRIQUOTE(ppycfLexer)
 *  -  void      ppycfLexer->ESCAPESEQ(ppycfLexer)
 *  -  void      ppycfLexer->INTEGER(ppycfLexer)
 *  -  void      ppycfLexer->LONGINT(ppycfLexer)
 *  -  void      ppycfLexer->DECIMALINTEGER(ppycfLexer)
 *  -  void      ppycfLexer->NONZERODIGIT(ppycfLexer)
 *  -  void      ppycfLexer->DIGIT(ppycfLexer)
 *  -  void      ppycfLexer->OCTINTEGER(ppycfLexer)
 *  -  void      ppycfLexer->HEXINTEGER(ppycfLexer)
 *  -  void      ppycfLexer->BININTEGER(ppycfLexer)
 *  -  void      ppycfLexer->OCTDIGIT(ppycfLexer)
 *  -  void      ppycfLexer->NONZEROOCTDIGIT(ppycfLexer)
 *  -  void      ppycfLexer->HEXDIGIT(ppycfLexer)
 *  -  void      ppycfLexer->BINDIGIT(ppycfLexer)
 *  -  void      ppycfLexer->FLOATNUMBER(ppycfLexer)
 *  -  void      ppycfLexer->POINTFLOAT(ppycfLexer)
 *  -  void      ppycfLexer->EXPONENTFLOAT(ppycfLexer)
 *  -  void      ppycfLexer->INTPART(ppycfLexer)
 *  -  void      ppycfLexer->FRACTION(ppycfLexer)
 *  -  void      ppycfLexer->EXPONENT(ppycfLexer)
 *  -  void      ppycfLexer->IMAGNUMBER(ppycfLexer)
 *  -  void      ppycfLexer->NAME(ppycfLexer)
 *  -  void      ppycfLexer->ID_START(ppycfLexer)
 *  -  void      ppycfLexer->ID_CONTINUE(ppycfLexer)
 *  -  void      ppycfLexer->STAR(ppycfLexer)
 *  -  void      ppycfLexer->DOUBLESTAR(ppycfLexer)
 *  -  void      ppycfLexer->LPAREN(ppycfLexer)
 *  -  void      ppycfLexer->RPAREN(ppycfLexer)
 *  -  void      ppycfLexer->LBRACK(ppycfLexer)
 *  -  void      ppycfLexer->RBRACK(ppycfLexer)
 *  -  void      ppycfLexer->LCURLY(ppycfLexer)
 *  -  void      ppycfLexer->RCURLY(ppycfLexer)
 *  -  void      ppycfLexer->COMMA(ppycfLexer)
 *  -  void      ppycfLexer->COLON(ppycfLexer)
 *  -  void      ppycfLexer->DOT(ppycfLexer)
 *  -  void      ppycfLexer->SEMI(ppycfLexer)
 *  -  void      ppycfLexer->ASSIGN(ppycfLexer)
 *  -  void      ppycfLexer->CONTINUED_LINE(ppycfLexer)
 *  -  void      ppycfLexer->NEWLINE(ppycfLexer)
 *  -  void      ppycfLexer->WS(ppycfLexer)
 *  -  void      ppycfLexer->LEADING_WS(ppycfLexer)
 *  -  void      ppycfLexer->COMMENT(ppycfLexer)
 *  -  void      ppycfLexer->DEDENT(ppycfLexer)
 *  -  void      ppycfLexer->INDENT(ppycfLexer)
 *  -  void      ppycfLexer->Tokens(ppycfLexer)
 *
 * The return type for any particular rule is of course determined by the source
 * grammar file.
 */
// [The "BSD licence"]
// Copyright (c) 2005-2009 Jim Idle, Temporal Wave LLC
// http://www.temporal-wave.com
// http://www.linkedin.com/in/jimidle
//
// All rights reserved.
//
// Redistribution and use in source and binary forms, with or without
// modification, are permitted provided that the following conditions
// are met:
// 1. Redistributions of source code must retain the above copyright
//    notice, this list of conditions and the following disclaimer.
// 2. Redistributions in binary form must reproduce the above copyright
//    notice, this list of conditions and the following disclaimer in the
//    documentation and/or other materials provided with the distribution.
// 3. The name of the author may not be used to endorse or promote products
//    derived from this software without specific prior written permission.
//
// THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
// IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
// OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
// IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
// INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
// NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
// DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
// THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
// (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
// THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

#ifndef	_pycfLexer_H
#define _pycfLexer_H
/* =============================================================================
 * Standard antlr3 C runtime definitions
 */
#include    <antlr3.h>

/* End of standard antlr 3 runtime definitions
 * =============================================================================
 */
 
#ifdef __cplusplus
extern "C" {
#endif

// Forward declare the context typedef so that we can use it before it is
// properly defined. Delegators and delegates (from import statements) are
// interdependent and their context structures contain pointers to each other
// C only allows such things to be declared if you pre-declare the typedef.
//
typedef struct pycfLexer_Ctx_struct pycfLexer, * ppycfLexer;



    #define ANTLR3_INLINE_INPUT_ASCII


#ifdef	ANTLR3_WINDOWS
// Disable: Unreferenced parameter,							- Rules with parameters that are not used
//          constant conditional,							- ANTLR realizes that a prediction is always true (synpred usually)
//          initialized but unused variable					- tree rewrite variables declared but not needed
//          Unreferenced local variable						- lexer rule declares but does not always use _type
//          potentially unitialized variable used			- retval always returned from a rule 
//			unreferenced local function has been removed	- susually getTokenNames or freeScope, they can go without warnigns
//
// These are only really displayed at warning level /W4 but that is the code ideal I am aiming at
// and the codegen must generate some of these warnings by necessity, apart from 4100, which is
// usually generated when a parser rule is given a parameter that it does not use. Mostly though
// this is a matter of orthogonality hence I disable that one.
//
#pragma warning( disable : 4100 )
#pragma warning( disable : 4101 )
#pragma warning( disable : 4127 )
#pragma warning( disable : 4189 )
#pragma warning( disable : 4505 )
#pragma warning( disable : 4701 )
#endif

/** Context tracking structure for pycfLexer
 */
struct pycfLexer_Ctx_struct
{
    /** Built in ANTLR3 context tracker contains all the generic elements
     *  required for context tracking.
     */
    pANTLR3_LEXER    pLexer;


     void (*mT__98)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__99)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__100)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__101)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__102)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__103)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__104)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__105)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__106)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__107)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__108)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__109)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__110)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__111)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__112)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__113)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__114)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__115)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__116)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__117)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__118)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__119)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__120)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__121)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__122)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__123)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__124)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__125)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__126)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__127)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__128)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__129)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__130)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__131)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__132)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__133)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__134)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__135)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__136)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__137)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__138)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__139)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__140)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__141)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__142)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__143)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__144)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__145)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__146)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__147)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__148)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__149)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__150)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__151)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__152)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__153)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__154)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__155)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__156)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__157)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__158)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__159)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__160)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mT__161)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mSTRINGLITERAL)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mSTRINGPREFIX)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mSHORTSTRING)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mLONGSTRING)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mBYTESLITERAL)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mBYTESPREFIX)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mSHORTBYTES)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mLONGBYTES)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mTRIAPOS)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mTRIQUOTE)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mESCAPESEQ)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mINTEGER)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mLONGINT)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mDECIMALINTEGER)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mNONZERODIGIT)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mDIGIT)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mOCTINTEGER)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mHEXINTEGER)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mBININTEGER)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mOCTDIGIT)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mNONZEROOCTDIGIT)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mHEXDIGIT)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mBINDIGIT)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mFLOATNUMBER)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mPOINTFLOAT)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mEXPONENTFLOAT)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mINTPART)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mFRACTION)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mEXPONENT)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mIMAGNUMBER)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mNAME)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mID_START)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mID_CONTINUE)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mSTAR)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mDOUBLESTAR)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mLPAREN)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mRPAREN)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mLBRACK)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mRBRACK)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mLCURLY)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mRCURLY)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mCOMMA)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mCOLON)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mDOT)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mSEMI)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mASSIGN)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mCONTINUED_LINE)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mNEWLINE)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mWS)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mLEADING_WS)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mCOMMENT)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mDEDENT)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mINDENT)	(struct pycfLexer_Ctx_struct * ctx);
     void (*mTokens)	(struct pycfLexer_Ctx_struct * ctx);    const char * (*getGrammarFileName)();
    void	    (*free)   (struct pycfLexer_Ctx_struct * ctx);
        

        ANTLR3_INT32    implicitLineJoiningLevel;
        ANTLR3_INT32    startPos;

        pANTLR3_STACK   identStack;
        pANTLR3_VECTOR  tokens;

        void (*origFree) ( struct pycfLexer_Ctx_struct *  ctx );
        pANTLR3_COMMON_TOKEN (*origNextToken)( pANTLR3_TOKEN_SOURCE  toksource );

};

// Function protoypes for the constructor functions that external translation units
// such as delegators and delegates may wish to call.
//
ANTLR3_API ppycfLexer pycfLexerNew         (pANTLR3_INPUT_STREAM instream);
ANTLR3_API ppycfLexer pycfLexerNewSSD      (pANTLR3_INPUT_STREAM instream, pANTLR3_RECOGNIZER_SHARED_STATE state);

/** Symbolic definitions of all the tokens that the lexer will work with.
 * \{
 *
 * Antlr will define EOF, but we can't use that as it it is too common in
 * in C header files and that would be confusing. There is no way to filter this out at the moment
 * so we just undef it here for now. That isn't the value we get back from C recognizers
 * anyway. We are looking for ANTLR3_TOKEN_EOF.
 */
#ifdef	EOF
#undef	EOF
#endif
#ifdef	Tokens
#undef	Tokens
#endif 
#define EXCEPT_STMT      37
#define EXPONENT      92
#define STAR      52
#define NONZERODIGIT      82
#define T__159      159
#define T__158      158
#define WHAT      23
#define TRIAPOS      73
#define NONZEROOCTDIGIT      87
#define T__160      160
#define LONGBYTES      77
#define EOF      -1
#define IMPORT_STMT      22
#define BREAK_STMT      11
#define T__161      161
#define LEADING_WS      97
#define DBL_STAR_ARG      34
#define RPAREN      50
#define OCTINTEGER      79
#define NAME_ARG      32
#define NAME      54
#define T__148      148
#define FINALLY_STMT      36
#define DICTIONARY      39
#define STRING_LITERAL      40
#define T__147      147
#define T__149      149
#define DOTTED_NAME      18
#define CONTINUE_STMT      12
#define BODY      8
#define T__154      154
#define COMMENT      48
#define T__155      155
#define SHORTBYTES      76
#define T__156      156
#define T__157      157
#define T__99      99
#define T__150      150
#define T__98      98
#define T__151      151
#define T__152      152
#define T__153      153
#define RBRACK      60
#define T__139      139
#define T__138      138
#define T__137      137
#define T__136      136
#define ARGUMENTS      46
#define ESCAPESEQ      72
#define LCURLY      61
#define FUNC_DEF      7
#define T__141      141
#define LIST      38
#define T__142      142
#define T__140      140
#define T__145      145
#define GLOBAL_STMT      21
#define T__146      146
#define T__143      143
#define T__144      144
#define T__126      126
#define SHORTSTRING      70
#define T__125      125
#define T__128      128
#define DECOR      17
#define T__127      127
#define WS      96
#define T__129      129
#define WHILE_STMT      28
#define INTPART      90
#define BINDIGIT      86
#define NOT_IN      41
#define BYTESLITERAL      68
#define FLOATNUMBER      65
#define LONGINT      64
#define PASS_STMT      10
#define T__130      130
#define T__131      131
#define T__132      132
#define T__133      133
#define T__134      134
#define T__135      135
#define EXPONENTFLOAT      89
#define CONTINUED_LINE      95
#define LBRACK      59
#define CLASS_INHERITANCE      45
#define DOUBLESTAR      53
#define ELSE_STMT      26
#define T__118      118
#define T__119      119
#define BYTESPREFIX      75
#define T__116      116
#define T__117      117
#define T__114      114
#define TRY_STMT      35
#define T__115      115
#define TEST_LIST      31
#define T__124      124
#define OCTDIGIT      84
#define T__123      123
#define BININTEGER      81
#define T__122      122
#define T__121      121
#define DEDENT      5
#define T__120      120
#define ELIF_STMT      27
#define DEL_STMT      9
#define PRINT_STMT      16
#define INDENT      4
#define WITH_STMT      30
#define LPAREN      49
#define POINTFLOAT      88
#define STRINGPREFIX      69
#define AS      24
#define IS_NOT      42
#define T__107      107
#define T__108      108
#define COMMA      51
#define T__109      109
#define T__103      103
#define IF_STMT      25
#define EXEC_STMT      20
#define T__104      104
#define T__105      105
#define T__106      106
#define T__111      111
#define T__110      110
#define T__113      113
#define T__112      112
#define DIGIT      83
#define DOT      58
#define IMAGNUMBER      66
#define RETURN_STMT      13
#define INTEGER      63
#define T__102      102
#define T__101      101
#define HEXINTEGER      80
#define T__100      100
#define STAR_ARG      33
#define SEMI      56
#define LONGSTRING      71
#define YIELD_STMT      15
#define COLON      55
#define TRIQUOTE      74
#define FOR_STMT      29
#define TRAILER_NAME      43
#define HEAD_NAME      44
#define ASSERT_STMT      19
#define NEWLINE      47
#define STRINGLITERAL      67
#define RCURLY      62
#define ASSIGN      57
#define ID_CONTINUE      94
#define DECIMALINTEGER      78
#define RAISE_STMT      14
#define FRACTION      91
#define ID_START      93
#define CLASS_DEF      6
#define HEXDIGIT      85
#ifdef	EOF
#undef	EOF
#define	EOF	ANTLR3_TOKEN_EOF
#endif

#ifndef TOKENSOURCE
#define TOKENSOURCE(lxr) lxr->pLexer->rec->state->tokSource
#endif

/* End of token definitions for pycfLexer
 * =============================================================================
 */
/** \} */

#ifdef __cplusplus
}
#endif

#endif

/* END - Note:Keep extra line feed to satisfy UNIX systems */
